# Math Tutor with LangChain and Groq

Welcome to the **Math Tutor** project! This repository contains a Python-based application that leverages the power of LangChain and Groq's LLM (Language Learning Model) to act as a virtual math tutor. The application is designed to help children aged 8 to 12 solve math problems by categorizing and answering their questions.

## Overview

The Math Tutor application uses a two-step process to handle user questions:

1. **Question Categorization**: The application first categorizes the user's question into either a "math" or "non_math" category. If the question is math-related, it proceeds to the next step. If not, it prompts the user to try again with a math question.

2. **Question Answering**: If the question is categorized as "math", the application uses a specialized prompt to solve the math problem or provide an appropriate answer.

The application is built using LangChain, a framework for developing applications powered by language models, and Groq's LLM, which provides the underlying language model capabilities.

## Features

- **Question Categorization**: Automatically categorizes user questions into "math" or "non_math".
- **Math Problem Solving**: Provides solutions to math problems for children aged 8 to 12.
- **JSON Output**: Saves the categorized question and its details in a JSON file for further processing.
- **User-Friendly Prompts**: Guides users to ask appropriate math-related questions.

## Installation

To get started with the Math Tutor application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/math-tutor-langchain.git
   ```

2. **Install Dependencies**:
   Install the required Python packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Groq API Key**:
   Replace `"your-groq-api-key"` in the `os.environ['GROQ_TOKEN']` line in the code with your actual Groq API key.

## Usage

1. **Run the Application**:
   Execute the Python script to start the Math Tutor:
   ```bash
   python math_tutor.py
   ```

2. **Input Your Question**:
   The application will prompt you to input a question. For example:
   ```plaintext
   Please, help me solve this equation: 5x2 + 2x + 2 = 0
   ```

3. **View the Results**:
   The application will categorize the question and provide an answer if it is math-related. The results will be displayed in the console and saved in a `question.json` file.

## Example Output

### Console Output:
```plaintext
{
    "keywords": {
        "question": "Please, help me solve this equation: 5x2 + 2x + 2 = 0",
        "category": "math"
    }
}
```

### JSON File (`question.json`):
```json
{
    "keywords": {
        "question": "Please, help me solve this equation: 5x2 + 2x + 2 = 0",
        "category": "math"
    }
}
```

### Answer:
```plaintext
{
    "answer": "The solution to the equation 5x^2 + 2x + 2 = 0 is complex. The roots are x = [-2 ± sqrt(4 - 40)] / 10, which simplifies to x = [-2 ± sqrt(-36)] / 10. Therefore, the roots are x = [-2 ± 6i] / 10, or x = -0.2 ± 0.6i."
}
```

## Customization

You can customize the prompts and the behavior of the application by modifying the `PromptTemplate` instances in the code. For example, you can adjust the temperature of the Groq LLM or change the model name to experiment with different language models.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- **LangChain**: For providing the framework to build applications with language models.
- **Groq**: For providing the powerful LLM that powers this application.

---

Thank you for using the Math Tutor application! We hope it helps make learning math fun and easy for children. If you have any questions or feedback, feel free to reach out.
