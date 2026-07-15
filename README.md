# Workplace Ethics Survey — Descriptive Analysis

A Python-based exploratory and descriptive analysis of a workplace ethics survey covering ethical culture, misconduct awareness, speaking-up behaviour, retaliation, organisational support, rule tolerance and concerns about the future of work.

The notebook analyses **667 survey responses** and converts a large set of coded questionnaire variables into interpretable labels, summary tables, visualisations and composite ethics indices.

## Project objectives

The analysis was designed to answer questions such as:

- How acceptable do employees consider different forms of workplace misconduct?
- How frequently are employees aware of ethical violations?
- Do employees report misconduct, and what happens after they speak up?
- What prevents employees from reporting concerns?
- How strong is the perceived ethical culture of organisations?
- What operational pressures encourage employees to compromise ethical standards?
- Do ethical attitudes differ by age, gender, sector or employment status?
- How concerned are employees about AI, technology and the future ethical environment of work?

## Analysis workflow

1. **Data inspection**
   - Reviewed data types, unique values and descriptive statistics.
   - Mapped coded demographic and survey responses to readable labels.

2. **Missing-value investigation**
   - Examined missingness against the survey's conditional question structure.
   - Identified that many missing responses were caused by questionnaire skip logic rather than random data loss.
   - For example, misconduct-detail questions were answered only by respondents aware of misconduct, while outcome questions were answered only by those who reported it.
   - The AI ethics guideline variable was excluded because of substantial non-applicable or missing responses and limited relevance to the main analysis.

3. **Univariate analysis**
   - Produced frequency tables, percentages and visualisations for demographics and individual ethics questions.

4. **Composite index development**
   - Recoded Likert-scale responses and calculated four respondent-level indices.

5. **Bivariate analysis**
   - Compared the indices and selected ethical outcomes across demographic and workplace groups using grouped summaries, cross-tabulations, box plots and stacked charts.

## Composite indices

| Index | Survey items | Interpretation | Mean |
|---|---|---|---:|
| **Ethical Acceptability Index (EAI)** | Eight Q1 scenarios | Higher values indicate greater acceptance of unethical behaviour | **2.23** |
| **Ethical Culture Index (ECI)** | Fourteen Q11 items | Higher values indicate a stronger perceived organisational ethical culture | **3.70** |
| **Rule Tolerance Index (RTI)** | Five Q14 items | Higher values indicate more permissive attitudes towards rule-breaking | **2.87** |
| **Future Ethical Concern Index (FECI)** | Nine Q15 items | Higher values indicate greater concern about future ethical issues | **2.96** |

All indices are calculated as respondent-level averages after recoding the relevant Likert responses. “Don't know” or “Prefer not to say” responses are excluded from index means.

## Key findings

### Ethical culture and misconduct

- **86.5%** of respondents said honesty was practised either *always* or *frequently* in their organisation.
- The Ethical Culture Index averaged **3.70 out of 5**, suggesting a generally positive perception of organisational ethics.
- **17.09%** of respondents had been aware of conduct that violated the law or their organisation's ethical standards during the previous year.
- Among the 114 respondents aware of misconduct, the most frequently observed issues were:
  - Bullying or harassment: approximately **39.5%**
  - Safety violations: approximately **36.0%**
  - Abuse of authority: approximately **30.7%**
  - Discrimination: approximately **25.4%**
  - Data misuse or privacy breaches: approximately **21.1%**

### Speaking up and organisational response

- **53.51%** of respondents who observed misconduct reported or raised their concerns.
- **42.98%** did not report it, while **3.51%** preferred not to say.
- Among the 61 respondents who reported misconduct, **63.94%** were very or fairly satisfied with the outcome.
- Despite this, **49.18%** experienced personal disadvantage or retaliation after speaking up.
- The leading reason for remaining silent was the belief that **no corrective action would be taken (61.2%)**. Fear of job loss and being labelled a troublemaker were also important barriers.

### Pressure and rule tolerance

- **11.09%** of respondents reported pressure to compromise ethical standards.
- Among those experiencing pressure, the most common drivers were:
  - Being asked to take shortcuts: **31.08%**
  - Time pressure or unrealistic deadlines: **29.73%**
  - Unrealistic business objectives: **25.68%**
  - Financial or budget pressure: **24.32%**
- Respondents showed moderate tolerance for minor rule breaches, but deliberate financial manipulation was strongly rejected.

### Demographic patterns

- Ethical tolerance declined consistently with age. The mean Ethical Acceptability Index fell from **2.61 for respondents aged 18–24** to **1.75 for respondents aged 65+**.
- Male respondents recorded slightly higher ethical acceptability and rule-tolerance scores than female respondents.
- Future ethical concern scores were broadly similar across genders.
- These are descriptive associations and should not be interpreted as causal relationships.

### Future ethical concerns

- The Future Ethical Concern Index averaged **2.96 out of 5**, indicating moderate overall concern.
- Respondents expressed concern about AI misuse, automation, workplace surveillance and the loss of interpersonal interaction, while generally viewing organisational governance and operational pressure as more immediate ethical risks than technology alone.

## Technologies used

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

## Repository contents

```text
Descriptive_Analysis_Ethics_Dataset/
├── Descriptive_Analysis_Ethics_Dataset.ipynb
└── README.md
```

## Running the notebook

The source CSV is not currently included in this repository. The notebook refers to a local file named `ethics_file.csv` using an absolute path.

1. Clone the repository:

```bash
git clone https://github.com/chandra56ashu/Descriptive_Analysis_Ethics_Dataset.git
cd Descriptive_Analysis_Ethics_Dataset
```

2. Install the required packages:

```bash
pip install pandas numpy matplotlib seaborn plotly jupyter
```

3. Place `ethics_file.csv` in an accessible local directory.

4. Replace the existing `pd.read_csv(...)` path in the notebook with the location of your CSV file, for example:

```python
df = pd.read_csv("ethics_file.csv")
```

5. Open and run the notebook:

```bash
jupyter notebook Descriptive_Analysis_Ethics_Dataset.ipynb
```

## Limitations

- The analysis is descriptive and does not establish causality.
- Several questions use conditional survey routing, so subgroup sample sizes differ substantially.
- High missingness in follow-up questions largely reflects skip logic and should not be interpreted as ordinary missing data.
- Small demographic categories, such as the “Other” gender group, are not large enough for reliable comparison.
- Some conclusions are based on self-reported perceptions and may be affected by social-desirability or non-disclosure bias.
- The raw dataset is not distributed in this repository.

## Author

**Ashutosh Chandra**  
MSc Business Data Analytics, Cranfield University  
[GitHub](https://github.com/chandra56ashu) · [Portfolio](https://chandra56ashu.github.io) · [LinkedIn](https://www.linkedin.com/in/ashutoshchandra8)
