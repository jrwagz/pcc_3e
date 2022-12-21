"""Sample Class for testing with pytest"""


class AnonymousSurvey:
    """Collect anonymous answers to a survey question"""

    def __init__(self, question: str) -> None:
        """Store a question, and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self) -> None:
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response: str) -> None:
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self) -> None:
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
