CONSTRUCTION_DICT = [{"role": "system", "content": "You will act as a summarization expert."},
                    {"role": "user", "content": ("Document: {document}\n\n"
                    "Your task is to read the Document and produce a succinct and accurate summary "
                    "that captures the key points and main arguments presented in the text.\n\nSummary:"),},
                    {"role": "assistant", "content": "{summary}",}
                    ]