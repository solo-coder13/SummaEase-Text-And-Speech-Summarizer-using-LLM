from bleuscore import calculate_bleu_score


f1 = open("/Users/gamingspectrum24/Documents/PRG/Projects/Full Stack/SummaEase-Text-And-Speech-Summarizer-using-LLM/Data/target_input.txt",'r')
f2 = open("/Users/gamingspectrum24/Documents/PRG/Projects/Full Stack/SummaEase-Text-And-Speech-Summarizer-using-LLM/Data/target_summary.txt",'r')
candidate = f1.read()
reference = f2.read()

print(calculate_bleu_score(candidate,reference))