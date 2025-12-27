# HAMong - Coding Agent Example

🤖 **Un esempio semplice di coding agent / A simple coding agent example**

## 🇮🇹 Descrizione (Italiano)

Questo progetto fornisce un esempio pratico di come funziona un **coding agent** (agente di codifica). Un coding agent è un programma che può:

- 📖 **Analizzare codice**: Leggere e comprendere file di codice
- 💡 **Suggerire miglioramenti**: Fornire consigli per migliorare la qualità del codice
- ✨ **Generare codice**: Creare automaticamente snippet di codice in vari linguaggi

### Funzionalità

L'agente di codifica HAMong può:

1. **Analizzare file di codice** e fornire metriche come:
   - Numero di righe
   - Numero di funzioni
   - Presenza di commenti
   - Suggerimenti per miglioramenti

2. **Generare codice** in diversi linguaggi:
   - Python
   - JavaScript
   - Java
   - C++

3. **Fornire template** per:
   - Hello World
   - Funzioni
   - Classi

### Come usarlo

```bash
# Eseguire l'esempio base
python coding_agent.py

# Eseguire la demo completa
python example_usage.py
```

### Esempio di codice

```python
from coding_agent import CodingAgent

# Creare un'istanza dell'agente
agent = CodingAgent("Il Mio Agente")

# Analizzare un file
analysis = agent.analyze_file("example.py")
print(f"Righe di codice: {analysis['line_count']}")
print(f"Suggerimenti: {analysis['suggestions']}")

# Generare codice
code = agent.generate_code("hello world", "python")
print(code)
```

---

## 🇬🇧 Description (English)

This project provides a practical example of how a **coding agent** works. A coding agent is a program that can:

- 📖 **Analyze code**: Read and understand code files
- 💡 **Suggest improvements**: Provide recommendations to improve code quality
- ✨ **Generate code**: Automatically create code snippets in various languages

### Features

The HAMong coding agent can:

1. **Analyze code files** and provide metrics such as:
   - Line count
   - Function count
   - Presence of comments
   - Improvement suggestions

2. **Generate code** in different languages:
   - Python
   - JavaScript
   - Java
   - C++

3. **Provide templates** for:
   - Hello World
   - Functions
   - Classes

### How to use

```bash
# Run the basic example
python coding_agent.py

# Run the full demo
python example_usage.py
```

### Code example

```python
from coding_agent import CodingAgent

# Create an agent instance
agent = CodingAgent("My Agent")

# Analyze a file
analysis = agent.analyze_file("example.py")
print(f"Lines of code: {analysis['line_count']}")
print(f"Suggestions: {analysis['suggestions']}")

# Generate code
code = agent.generate_code("hello world", "python")
print(code)
```

---

## 📦 Requirements / Requisiti

- Python 3.6 or higher / Python 3.6 o superiore
- No external dependencies required / Nessuna dipendenza esterna richiesta

## 🚀 Quick Start / Avvio Rapido

```bash
# Clone the repository / Clona il repository
git clone https://github.com/saveriocarlogreco/HAMong.git
cd HAMong

# Run the example / Esegui l'esempio
python coding_agent.py

# Or run the full demo / O esegui la demo completa
python example_usage.py
```

## 📝 What is a Coding Agent? / Cos'è un Coding Agent?

### 🇮🇹 Italiano

Un **coding agent** (agente di codifica) è un programma intelligente che può:
- Comprendere il codice sorgente
- Analizzare la qualità e struttura del codice
- Generare nuovo codice automaticamente
- Suggerire miglioramenti e best practices

Gli agenti di codifica sono utili per:
- 🎓 **Apprendimento**: Aiutare i principianti a imparare buone pratiche
- 🔍 **Revisione del codice**: Identificare potenziali problemi
- ⚡ **Automazione**: Generare codice boilerplate velocemente
- 💡 **Assistenza**: Fornire suggerimenti durante lo sviluppo

### 🇬🇧 English

A **coding agent** is an intelligent program that can:
- Understand source code
- Analyze code quality and structure
- Generate new code automatically
- Suggest improvements and best practices

Coding agents are useful for:
- 🎓 **Learning**: Help beginners learn good practices
- 🔍 **Code review**: Identify potential issues
- ⚡ **Automation**: Generate boilerplate code quickly
- 💡 **Assistance**: Provide suggestions during development

## 🔧 Implementation Details / Dettagli Implementazione

The agent uses:
- Regular expressions for code pattern matching
- Template-based code generation
- File analysis algorithms

L'agente utilizza:
- Espressioni regolari per il pattern matching del codice
- Generazione di codice basata su template
- Algoritmi di analisi dei file

## 📄 License / Licenza

This project is open source and available for educational purposes.
Questo progetto è open source e disponibile per scopi educativi.

---

**Made with ❤️ by Saverio Carlo Greco**