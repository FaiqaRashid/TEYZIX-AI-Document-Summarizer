import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
from datetime import datetime

# Download required packages for NLTK
nltk.download('punkt_tab')
nltk.download('stopwords')

def get_direct_input():
    """Gets multi-line text input from the user in the console."""
    print("\n--- Direct Text Input ---")
    print("Paste or type your text below. Type 'DONE' on a new line when finished:")
    
    lines = []
    while True:
        line = input()
        if line.strip() == "DONE":
            break
        lines.append(line)
        
    # Join all lines back together with newline characters
    text = "\n".join(lines)
    return text.strip()

def read_file(filename):
    """Reads content from a .txt file with proper error handling."""
    try:
        with open(filename,'r',encoding='utf-8') as f:
             return f.read().strip()
    except FileNotFoundError:
        print("File not Found ")
        return None
    
def data_input_system():
    """Main orchestrator for the Data Input System."""
    print("====================================")
    print("   AI DOCUMENT SUMMARIZER SYSTEM   ")
    print("====================================")
    print("Select an input method:")
    print("1. Direct User Input")
    print("2. Load from Text File (.txt)")
    #get user Choice
    ch=input("(Enter Your Choice(1-2):)").strip()
    if ch=="1":
        return get_direct_input()
    elif ch=="2":
       filename = input("Enter the path to your .txt file: ").strip()
       return read_file(filename)
    else:
        print("Invalid Choice. Please Select(1-2)")
        return None
    

def process_raw_data(rawtext):
    sentences=sent_tokenize(rawtext)
    words=word_tokenize(rawtext.lower())
    stop_words=set(stopwords.words('english'))
    clean_words=[]
    for word in words:
        if word.isalnum() and word not in stop_words:
            clean_words.append(word)
    return sentences , clean_words    

def calculate_word_frequencies(cleaned_words):
    """Calculates the weighted frequency of each content word."""
    # 1. Count raw frequencies automatically using Counter
    word_counts = Counter(cleaned_words)
    
    # 2. Find the count of the absolute most frequent word
    max_frequency = max(word_counts.values()) if word_counts else 1
    
    # 3. Normalize frequencies (divide each count by max_frequency)
    weighted_frequencies = {}
    for word, count in word_counts.items():
        weighted_frequencies[word] = count / max_frequency
        
    return weighted_frequencies

def score_sentences(sentences, weighted_frequencies):
    """Scores each sentence based on the weighted values of its words."""
    sentence_scores = {}
    
    for sentence in sentences:
        # Tokenize the individual sentence into lowercase words for look-up
        words_in_sentence = word_tokenize(sentence.lower())
        
        # Only score sentences that are not completely empty and reasonably sized
        if len(words_in_sentence) < 30:
            for word in words_in_sentence:
                if word in weighted_frequencies:
                    # If the sentence isn't in our dictionary yet, initialize it
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = weighted_frequencies[word]
                    else:
                        sentence_scores[sentence] += weighted_frequencies[word]
                        
    return sentence_scores

def generate_summary(sentences, sentence_scores, percentage):
    """Selects the top-ranked sentences and arranges them in original order."""
    if not sentence_scores:
        return "Could not generate a summary. The text might be too short or invalid."
    
    # 1. Sort sentences by score in descending order
    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    
    # 2. Calculate how many sentences to include based on user percentage
    num_sentences = max(1, int(len(sentences) * (percentage / 100)))
    
    # 3. Take the top 'n' sentences
    top_sentences = ranked_sentences[:num_sentences]
    
    # 4. Sort them back into their original chronological order so it reads well
    summary_sentences = sorted(top_sentences, key=sentences.index)
    
    # Join them back into a single clean string block
    return "\n".join(summary_sentences)

def export_summary(summary_text, output_filename):
    """Saves the generated summary into a local text file with a custom name."""
    try:
        # Ensure the filename ends with .txt
        if not output_filename.endswith(".txt"):
            output_filename += ".txt"
            
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(summary_text)
        print(f"\n💾 Success! Summary exported successfully to '{output_filename}'")
    except Exception as e:
        print(f"❌ Error exporting the file: {e}")

def display_comparison(original_text, summary_text):
    """Displays side-by-side style comparison metrics to the console."""
    print("\n====================================")
    print("        SUMMARIZATION REPORT        ")
    print("====================================")
    print(f"Original Character Count: {len(original_text)}")
    print(f"Summary Character Count: {len(summary_text)}")
    print(f"Reduction Rate: {100 - (len(summary_text)/len(original_text)*100):.1f}% smaller")
    print("------------------------------------")
    print("📝 GENERATED SUMMARY:")
    print(summary_text)
    print("====================================")

def main():
    # Step 1: Get the raw text using Chunk 1
    raw_text = data_input_system()
    if not raw_text:
        print("No text provided. Exiting program.")
        return
        
    # Step 2: Preprocess using Chunk 2
    sentences, cleaned_words = process_raw_data(raw_text)
    
    # Step 3: Compute math scores using Chunk 3
    weighted_freqs = calculate_word_frequencies(cleaned_words)
    sentence_scores = score_sentences(sentences, weighted_freqs)
    
    # Step 4: Ask the user for their custom length constraint
    try:
        user_pct = int(input("\nEnter summary length percentage (e.g., 20 for 20%, 40 for 40%): ").strip())
        if not (5 <= user_pct <= 90):
            print("Using default value of 30% due to out-of-range input.")
            user_pct = 30
    except ValueError:
        print("Invalid input. Using default value of 30%.")
        user_pct = 30
        
    # Step 5: Generate and export using Chunk 4 & 5
    summary = generate_summary(sentences, sentence_scores, user_pct)
    display_comparison(raw_text, summary)
    
    # Ask if they want to save it
    save_choice = input("Do you want to export this summary to a .txt file? (y/n): ").strip().lower()
    if save_choice == 'y':
        # 🌟 UPDATED: Dynamic filename input to prevent file overwriting
        custom_name = input("Enter a unique name for your summary file (e.g., ai_summary, cs_summary): ").strip()
        if not custom_name:
            custom_name = "summary"  # Safe default if the user hits Enter accidentally
            
        export_summary(summary, custom_name)

# This line ensures the script runs when executed from the terminal
if __name__ == "__main__":
    main()