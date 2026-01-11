┌────────────┐
│ User Query │
└─────┬──────┘
      │
┌─────────────────────┐
│ Query Understanding │  ← Zero-shot classification
│  - Intent           │
│  - Ambiguity        │
│  - Freshness need   │
└─────┬───────────────┘
      │
┌─────────────────────┐
│ Decision Agent      │  ← Policy-driven
│  (LLM-based)        │
└─────┬───────────────┘
      │
 ┌────┴────┬──────────┬─────────┬─────────┐
 │ LLM     │ RAG      │ Web     │ Hybrid  │
 │ only    │ pipeline │ Search  │         │
 └─────────┴──────────┴─────────┴─────────┘
      │
┌─────────────────────┐
│ Answer Synthesizer  │
│ + Citations         │
│ + Confidence Score  │
└─────────┬───────────┘
          │
      Final Answer