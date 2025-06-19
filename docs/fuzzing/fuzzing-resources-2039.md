---
title: "Fuzzing Resources 2039"
category: "Fuzzing"
source_url: ""
date_collected: 2025-06-25
license: "CC-BY-4.0"
---

The references below extend [fuzzing-resources-2038.md](fuzzing-resources-2038.md) with additional papers, blog posts and repositories on fuzzing techniques for large language models.

- [AFL project](https://github.com/google/AFL) – classic fuzzing engine often combined with LLM-guided mutation.
- [AFL++](https://github.com/AFLplusplus/AFLplusplus) – modern fork with advanced instrumentation used by several LLM fuzzing efforts.
- [GPTFuzz Mutation Analysis](https://github.com/sherdencooper/GPTFuzz.B.MutationAnalysisToinvestigatewhyPROMPTFUZZimprovesperformancewithinitialseeds) – explores how prompt mutations impact success rates.
- [Lakera GandalfIgnoreInstructions dataset](https://huggingface.co/datasets/Lakera/gandalfignoreinstructions) – corpus for evaluating instruction-resistant prompts.
- [BlackHat Asia 2025 talk: LLM Zero Day Fuzzing](https://www.blackhat.com/asia-25/briefings/schedule/index.html#llm-zero-day-fuzzing-102) – conference presentation covering zero-day discovery via LLM fuzzing.
