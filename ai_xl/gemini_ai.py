from google import genai


class GeminiAI:

    def _init_(self):

        api_key = input("Enter your Gemini API Key: ").strip()

        self.client = genai.Client(api_key=api_key)

    def generate_summary(self, data, stats):

        prompt = f"""
You are an expert Business Analyst.

Employee Sales Data:
{data}

Statistics

Total Sales : {stats['total']}
Average Sales : {stats['average']}
Highest Sales : {stats['highest']}
Lowest Sales : {stats['lowest']}

Top Performer : {stats['highest_employee']}
Lowest Performer : {stats['lowest_employee']}

Generate a professional monthly sales report.

Include:

1. Overall Summary
2. Performance Analysis
3. Key Observations
4. Business Insights
5. Suggestions
6. Conclusion

Keep the report professional and easy to understand.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    def ask_question(self, data, stats, question):

        prompt = f"""
You are an AI Data Analyst.

Employee Sales Data

{data}

Statistics

Total Sales : {stats['total']}
Average Sales : {stats['average']}
Highest Sales : {stats['highest']}
Lowest Sales : {stats['lowest']}

Top Performer : {stats['highest_employee']}
Lowest Performer : {stats['lowest_employee']}

Answer only using the above data whenever possible.

User Question:
{question}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    def chat(self, data, stats):

        print("\n===================================")
        print("      GEMINI AI ASSISTANT")
        print("===================================")
        print("Ask anything about the report.")
        print("Examples:")
        print("- Who is the top performer?")
        print("- Who is below average?")
        print("- Give suggestions.")
        print("- Predict next month's sales.")
        print("- Which employee needs improvement?")
        print("Type 'exit' to quit.")
        print("===================================\n")

        while True:

            question = input("You : ")

            if question.lower() == "exit":
                print("\nExiting AI Chat...\n")
                break

            try:

                answer = self.ask_question(
                    data,
                    stats,
                    question
                )

                print("\nGemini:\n")
                print(answer)
                print()

            except Exception as e:

                print("\nError:", e)
