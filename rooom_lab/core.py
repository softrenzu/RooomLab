from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True, slots=True)
class Cell:
    id:str; code:str

class ReactiveNotebook:
    def __init__(self): self.cells={}; self.outputs={}; self.namespace={}
    def add(self,cell:Cell)->None:
        if cell.id in self.cells: raise ValueError('duplicate cell id')
        ast.parse(cell.code); self.cells[cell.id]=cell
    def _defs_uses(self,cell:Cell)->tuple[set[str],set[str]]:
        tree=ast.parse(cell.code); defs=set(); uses=set()
        for node in ast.walk(tree):
            if isinstance(node,(ast.FunctionDef,ast.ClassDef)): defs.add(node.name)
            elif isinstance(node,ast.Name):
                (defs if isinstance(node.ctx,ast.Store) else uses).add(node.id)
        return defs,uses-defs
    def order(self)->list[str]:
        meta={cid:self._defs_uses(c) for cid,c in self.cells.items()}; producers={}
        for cid,(defs,_) in meta.items():
            for name in defs: producers[name]=cid
        deps={cid:{producers[u] for u in uses if u in producers and producers[u]!=cid} for cid,(_,uses) in meta.items()}
        order=[]; remaining=set(self.cells)
        while remaining:
            ready=sorted(cid for cid in remaining if not (deps[cid]&remaining))
            if not ready: raise ValueError('cyclic dependency')
            order.extend(ready); remaining-=set(ready)
        return order
    def run(self)->dict[str,Any]:
        for cid in self.order():
            code=self.cells[cid].code; tree=ast.parse(code)
            last=tree.body[-1] if tree.body else None
            if isinstance(last,ast.Expr):
                prefix=ast.Module(body=tree.body[:-1],type_ignores=[]); exec(compile(prefix,'<cell>','exec'),self.namespace)
                value=eval(compile(ast.Expression(last.value),'<cell>','eval'),self.namespace); self.outputs[cid]=value
            else:
                exec(compile(tree,'<cell>','exec'),self.namespace); self.outputs[cid]=None
        return dict(self.outputs)
