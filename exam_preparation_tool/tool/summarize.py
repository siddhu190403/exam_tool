import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summarize_text(text, max_sentences):
    # Load the spaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Process the input text
    doc = nlp(text)

    # Calculate the importance of each sentence using the default spaCy model
    sentence_scores = []
    for sentence in doc.sents:
        sentence_score = 0
        for word in sentence:
            sentence_score += word.vector_norm
        sentence_scores.append((sentence, sentence_score))

    # Sort sentences by importance and select the top N sentences
    sentence_scores.sort(key=lambda x: x[1], reverse=True)
    selected_sentences = [s[0].text for s in sentence_scores[:max_sentences]]

    # Join the selected sentences to create the summary
    summary = " ".join(selected_sentences)

    return summary

def summarize(input_text, num_sentences=3):
    # Initialize a LexRank summarizer
    summarizer = LexRankSummarizer()

    # Parse the input text
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))

    # Get the summary with the specified number of sentences
    summary = summarizer(parser.document, num_sentences)

    # Combine the summary sentences into a single string
    summary_text = " ".join([str(sentence) for sentence in summary])

    return summary_text