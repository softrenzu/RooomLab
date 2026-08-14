# ROOOMTECH AI Stack

**A growing source-available AI software stack built in Japan.**

ROOOMTECH is building a set of independent tools for RAG, AI agents, LLM routing, inference, identity, observability, developer workflows, multimodal data, and real-world AI applications.

The goal is simple: build useful software, publish it, let people try it, break it, improve it, and help shape what comes next.

> The projects are at different maturity levels and are not all production-ready or fully integrated with one another yet. Check each repository for its current status, version, roadmap, tests, and license.

## Start here

| Project | What it does | Repository |
|---|---|---|
| **RooomAgent** | Business AI-agent runtime with RAG, tools, approvals, audit trails, long-term memory, reusable skills, feedback and sub-agent analysis | https://github.com/softrenzu/RooomAgent |
| **RooomRAG** | Document ingestion, retrieval, context construction and cited LLM answers | https://github.com/softrenzu/RooomRAG |
| **RooomVector** | Vector database focused on RAG and Dify workloads, including hybrid retrieval and explainable search | https://github.com/softrenzu/RooomVector |

## Stack map

```text
Applications / Users
        |
        +---- RooomUI -------- human interaction / approvals
        |
        +---- Hostbot -------- hospitality AI application
        |
        v
    RooomAgent -------- business AI agent runtime
        |
        +---- RooomMemory ---- long-term agent memory
        +---- RooomRAG ------- retrieval-augmented generation
        |       |
        |       +---- RooomParse ---- document normalization
        |       +---- RooomWeb ------ governed web collection
        |       +---- RooomVector --- vector + hybrid retrieval
        |
        +---- RooomRoute ----- multi-LLM routing
        +---- RooomGateway --- enterprise LLM API gateway
        +---- RooomInfer ----- inference control plane
        |
        +---- RooomGate ------ identity + authorization
        |
        +---- RooomObserve --- LLM/agent operations
        +---- RooomMetrics --- metrics
        +---- RooomLog ------- logs

Developer / Model layer
        +---- RooomDevFlow --- agentic software-delivery governance
        +---- RooomCoder ----- policy-aware coding-agent controls
        +---- RooomTrain ----- model-training control plane
        +---- RooomVision ---- visual-dataset catalog
        +---- RooomVoice ----- local voice-AI controls
        +---- RooomLab ------- reactive Python notebook core
```

This diagram shows the intended product layers. Integration maturity varies by repository.

## AI agents, RAG and knowledge

| Project | Focus | Repository |
|---|---|---|
| **RooomAgent** | Knowledge-grounded business agents, tools, approvals, audit, memory and reusable skills | https://github.com/softrenzu/RooomAgent |
| **RooomRAG** | RAG ingestion, search, chat and citations across business documents | https://github.com/softrenzu/RooomRAG |
| **RooomVector** | Hybrid vector retrieval, metadata filters, HNSW/IVFFlat, quantization, reranking and Dify integration | https://github.com/softrenzu/RooomVector |
| **RooomMemory** | Tenant-aware long-term memory with retrieval, retention and auditable deletion | https://github.com/softrenzu/RooomMemory |
| **RooomParse** | Governed document parsing and normalization for AI/RAG pipelines | https://github.com/softrenzu/RooomParse |
| **RooomWeb** | Policy-controlled public-web collection for AI, RAG, monitoring and research workflows | https://github.com/softrenzu/RooomWeb |

## LLM routing and inference

| Project | Focus | Repository |
|---|---|---|
| **RooomRoute** | Explainable multi-LLM routing using quality, cost, latency, policy, region and provider diversity | https://github.com/softrenzu/RooomRoute |
| **RooomGateway** | Enterprise OpenAI-compatible LLM gateway with privacy, reliability, budget and routing controls | https://github.com/softrenzu/RooomGateway |
| **RooomInfer** | Adaptive LLM inference control plane around engines such as vLLM | https://github.com/softrenzu/RooomInfer |

## Security and governance

| Project | Focus | Repository |
|---|---|---|
| **RooomGate** | Identity and authorization with RBAC, ABAC, ReBAC, workload/agent identity and explainable decisions | https://github.com/softrenzu/RooomGate |
| **RooomDevFlow** | Governance for agentic software delivery, including policies, approvals, budgets, provider routing and audit | https://github.com/softrenzu/RooomDevFlow |
| **RooomCoder** | Policy-aware coding-agent controls for repository context, planning, secret detection and approvals | https://github.com/softrenzu/RooomCoder |

## Observability

| Project | Focus | Repository |
|---|---|---|
| **RooomObserve** | LLM and agent operations: traces, anomaly detection, cost, regression comparison and remediation hints | https://github.com/softrenzu/RooomObserve |
| **RooomMetrics** | Multi-tenant metrics engine with cardinality protection, replication, distributed reads and anomaly detection | https://github.com/softrenzu/RooomMetrics |
| **RooomLog** | Search-first log engine with structured search, live tail, OTLP ingestion and Loki migration endpoints | https://github.com/softrenzu/RooomLog |

## Model, data and interaction tools

| Project | Focus | Repository |
|---|---|---|
| **RooomTrain** | Model-training control plane for experiment specs, GPU estimates, reproducible manifests and job tracking | https://github.com/softrenzu/RooomTrain |
| **RooomVision** | Versioned visual-dataset catalog with integrity hashes, deterministic splits, annotations and duplicate detection | https://github.com/softrenzu/RooomVision |
| **RooomVoice** | Local voice-AI control core with audio inspection, segmentation, consent records and engine adapters | https://github.com/softrenzu/RooomVoice |
| **RooomUI** | Agent-native UI interaction layer with shared state, generative UI events, tool requests and human approvals | https://github.com/softrenzu/RooomUI |
| **RooomLab** | Reproducible reactive Python cell engine with dependency analysis and deterministic execution | https://github.com/softrenzu/RooomLab |

## Vertical application

### Hostbot

AI operations platform for hotels, vacation rentals and accommodation businesses. It combines guest AI, reservation verification, server-side policy, incident workflows, support tickets, audit logs and connector interfaces.

https://github.com/softrenzu/Hostbot

## Why build this stack?

AI systems need more than a model endpoint. Real deployments need retrieval, permissions, approvals, routing, observability, cost controls, data ingestion, memory, developer governance and application-specific workflows.

ROOOMTECH is exploring those layers as separate, independently maintainable projects so each component can evolve without requiring one monolithic platform.

## Try it. Break it. Improve it.

If you are an AI engineer, developer, researcher, startup or technical team anywhere in the world:

- Try a project that matches your problem.
- Open an Issue when something is unclear or broken.
- Send a Pull Request when you can improve it.
- Suggest integrations, benchmarks and missing features.
- Share what you built with it.

GitHub profile: https://github.com/softrenzu

## Licensing and commercial use

These repositories are **source-available projects**. They should not automatically be described as OSI-approved open source.

Licensing differs by repository and release. Many ROOOMTECH-authored projects permit defined noncommercial uses while requiring a separate paid ROOOMTECH commercial software license for business, production or other commercial-purpose use outside those permissions.

Always check the `LICENSE`, commercial-license documents and third-party notices in the specific repository and version you intend to use.

Commercial licensing, implementation, integration, private builds, maintenance and support are available from ROOOMTECH.

Contact: **support@rooomtech.com**

## From Japan, for builders everywhere

We are building in public and want real-world feedback.

**Use it. Test it. Challenge it. Help make it better.**
