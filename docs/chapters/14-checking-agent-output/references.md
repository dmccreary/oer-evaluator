# References: Checking and Calibrating AI Agent Output

1. [Hallucination (artificial intelligence)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) - Wikipedia - Explains how AI systems produce confident but false output, including invented citations, and why it happens. Background for the chapter's sections on hallucination and invented citation.

2. [Cohen's kappa](https://en.wikipedia.org/wiki/Cohen%27s_kappa) - Wikipedia - Defines Cohen's kappa, which measures agreement between two raters beyond chance, with a worked example. Supports the chapter's measures of agreement between an agent and human reviewers.

3. [Calibration (statistics)](https://en.wikipedia.org/wiki/Calibration_(statistics)) - Wikipedia - Explains calibration as the match between stated confidence and observed accuracy. Background for detecting overconfident scores and for calibrating an agent against human reviewers.

4. Superforecasting: The Art and Science of Prediction - Philip E. Tetlock and Dan Gardner - Crown (2015) - Tetlock's forecasting tournaments score stated confidence against outcomes, showing who is well calibrated. Checking confidence against results is the same logic used to calibrate an agent's scores.

5. Handbook of Inter-Rater Reliability (4th ed.) - Kilem L. Gwet - Advanced Analytics (2014) - Gwet devised the AC1 statistic to fix the kappa paradox, in which high raw agreement can still yield a low kappa. The handbook explains agreement measures with worked examples.

6. [Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629) - arXiv - Ji and colleagues' survey sorts hallucinations into types and reviews how they are measured and reduced. Gives vocabulary for classifying an agent's errors.

7. [Reduce Hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) - Claude Platform Docs - Practical prompt techniques such as letting the model say it does not know, asking for direct quotes, and verifying claims. Supports the chapter's verification steps.

8. [Interrater Reliability: The Kappa Statistic](https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/) - Biochemia Medica - McHugh explains kappa in plain terms, how to interpret its values, and where it misleads. A readable companion to the chapter's section on measuring agreement.

9. [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) - arXiv - Kadavath and colleagues test whether a model's stated confidence matches how often it is right. Useful background on why overconfident scores can be checked rather than just feared.

10. [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) - arXiv - Measures how often model judges agree with human raters and documents biases such as position and verbosity. Informs the chapter's second-agent cross-check and its limits.
