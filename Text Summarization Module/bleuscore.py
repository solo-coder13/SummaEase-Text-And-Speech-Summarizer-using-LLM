import nltk
nltk.download('punkt')
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.tokenize import word_tokenize

def calculate_bleu_score(candidate, reference):
    candidate_tokens = word_tokenize(candidate)
    reference_tokens = [word_tokenize(ref) for ref in reference]
    smoothing_function = SmoothingFunction().method4
    return sentence_bleu(reference_tokens, candidate_tokens, smoothing_function=smoothing_function)