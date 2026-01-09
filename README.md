# AI_Calculator
A machine learning experiment that attempts to solve arithmetic problems (specifically addition) by treating mathematical equations as text classification tasks rather than numerical computations.

This project uses **Scikit-Learn** to build a pipeline consisting of a `CountVectorizer` and a `MultinomialNB` (Naive Bayes) classifier to predict the result of an equation based on its string representation.

---

### **Features**

* **Automated Dataset Generation:** Generates random addition problems for training and testing.
* **NLP Pipeline:** Converts mathematical strings (e.g., "10+5") into vectors to train a Naive Bayes model.
* **Accuracy Tracking:** Calculates and prints the percentage of correct predictions.
* **Detailed Logging:** Saves every prediction, the actual answer, and a correctness boolean to an output file.

---

### **Project Structure**

* `main.py`: The core script that reads data, trains the model, performs predictions, and calculates accuracy.
* `testcasege.py`: A helper script that generates random addition equations and splits them into training (`dat.txt`) and testing (`test.txt`) files.
* `requirements.txt`: Lists the Python dependencies required to run the project.
* `dat.txt` / `test.txt`: (Generated) The dataset files containing equations in `Equation=Result` format.
* `out.txt`: (Generated) The output log showing the model's predictions vs. actual results.

---

### **Installation**

1. **Clone the repository** (or download the files).
2. **Install dependencies**:
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt

```



---

### **Usage**

Follow these steps to run the project:

#### **1. Generate the Dataset**

Before training, you need to create the training and testing data. Run the test case generator:

```bash
python testcasege.py

```

*This will create `dat.txt` (Training Data) and `test.txt` (Testing Data) in your directory.*

#### **2. Train and Predict**

Run the main script to train the model and see the results:

```bash
python main.py

```

**Output Example:**

```text
Number of correct guesses;  44
Total number of guesses: 813
Percentage of correct sol:  5.412054120541206 %

```

#### **3. Analyze Results**

Check the `out.txt` file to see exactly which equations the model got right or wrong.

```text
1 Prediction :
10+5=15 correct? True

2 Prediction :
3+3=8 correct? False

```

---

### **How it Works**

1. **Data Generation:** The generator creates strings in the format `A+B=C`.
2. **Preprocessing:** The code splits these strings. `A+B` becomes the input (feature), and `C` becomes the target label.
3. **Vectorization:** `CountVectorizer` treats numbers and symbols as "words," converting the equation string into a frequency vector.
4. **Classification:** `MultinomialNB` learns the probability of a specific result (Label) occurring given the tokens in the equation.
5. **Prediction:** The model predicts the result class (the sum) for the testing set.
