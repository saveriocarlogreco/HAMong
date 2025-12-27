"""
Simple Coding Agent Example
Un esempio semplice di coding agent / A simple coding agent example

This is a basic implementation of a coding agent that can:
- Analyze code files
- Suggest improvements
- Generate simple code snippets
"""

import os
import re
from typing import List, Dict, Any


class CodingAgent:
    """
    A simple coding agent that can analyze and generate code.
    Un semplice agente di codifica che può analizzare e generare codice.
    """
    
    MAX_LINE_LENGTH = 100  # Maximum recommended line length
    
    def __init__(self, name: str = "CodingAgent"):
        self.name = name
        self.supported_languages = ["python", "javascript", "java", "cpp"]
        
    def analyze_file(self, filepath: str) -> Dict[str, Any]:
        """
        Analyze a code file and provide insights.
        Analizza un file di codice e fornisce informazioni.
        
        Args:
            filepath: Path to the file to analyze
            
        Returns:
            Dictionary with analysis results
        """
        if not os.path.exists(filepath):
            return {"error": f"File not found: {filepath}"}
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except (IOError, PermissionError, UnicodeDecodeError) as e:
            return {"error": f"Error reading file: {str(e)}"}
        
        lines = content.split('\n')
        analysis = {
            "filename": os.path.basename(filepath),
            "line_count": len(lines),
            "char_count": len(content),
            "has_comments": self._has_comments(content),
            "functions": self._count_functions(content),
            "suggestions": self._generate_suggestions(content, filepath)
        }
        
        return analysis
    
    def _has_comments(self, content: str) -> bool:
        """Check if code has comments."""
        # Simple check for common comment patterns
        # Using separate checks for better reliability
        if re.search(r'#.*', content):  # Python, Shell
            return True
        if re.search(r'//.*', content):  # C, C++, Java, JavaScript
            return True
        if re.search(r'/\*', content) and re.search(r'\*/', content):  # Block comments
            return True
        return False
    
    def _count_functions(self, content: str) -> int:
        """Count function definitions in the code."""
        # Simple pattern matching for function definitions
        patterns = [
            r'\bdef\s+\w+\s*\(',  # Python
            r'\bfunction\s+\w+\s*\(',  # JavaScript
            r'\b\w+\s+\w+\s*\([^)]*\)\s*\{',  # Java/C++
        ]
        
        count = 0
        for pattern in patterns:
            count += len(re.findall(pattern, content))
        
        return count
    
    def _generate_suggestions(self, content: str, filepath: str) -> List[str]:
        """Generate improvement suggestions for the code."""
        suggestions = []
        
        # Check for missing comments
        if not self._has_comments(content):
            suggestions.append("Considera l'aggiunta di commenti / Consider adding comments to explain the code")
        
        # Check for very long lines
        lines = content.split('\n')
        long_lines = [(i + 1, len(line)) for i, line in enumerate(lines) if len(line) > self.MAX_LINE_LENGTH]
        if long_lines:
            examples = long_lines[:3]
            line_info = ", ".join([f"{line}({length})" for line, length in examples])
            suggestions.append(f"Alcune righe sono molto lunghe (>{self.MAX_LINE_LENGTH} caratteri): {line_info} / "
                             f"Some lines are very long (>{self.MAX_LINE_LENGTH} chars): {line_info}")
        
        # Check for empty file
        if len(content.strip()) == 0:
            suggestions.append("Il file è vuoto / The file is empty")
        
        # Check file extension for docstrings (Python)
        if filepath.endswith('.py'):
            if '"""' not in content and "'''" not in content:
                suggestions.append("Considera l'aggiunta di docstrings / Consider adding docstrings to functions and classes")
        
        return suggestions if suggestions else ["Il codice sembra buono! / Code looks good!"]
    
    def get_comment_header(self, language: str, text: str) -> str:
        """
        Get a properly formatted comment header for a given language.
        Ottiene un'intestazione di commento formattata correttamente per un dato linguaggio.
        
        Args:
            language: Programming language (python, javascript, java, cpp)
            text: Text to include in the comment
            
        Returns:
            Formatted comment string
        """
        if language.lower() == "python":
            lines = text.split('\n')
            return '\n'.join([f"# {line}" for line in lines]) + '\n'
        else:
            lines = text.split('\n')
            return '\n'.join([f"// {line}" for line in lines]) + '\n'
    
    def generate_code(self, description: str, language: str = "python") -> str:
        """
        Generate simple code based on a description.
        Genera codice semplice basato su una descrizione.
        
        Args:
            description: What the code should do
            language: Programming language (python, javascript, etc.)
            
        Returns:
            Generated code as string
        """
        if language.lower() not in self.supported_languages:
            return f"# Language '{language}' not supported yet"
        
        # Simple template-based generation for demo purposes
        templates = {
            "hello world": self._generate_hello_world,
            "function": self._generate_function,
            "class": self._generate_class,
        }
        
        # Match description to template
        description_lower = description.lower()
        for key, generator in templates.items():
            if key in description_lower:
                return generator(language)
        
        # Default response
        return f"# Generated code for: {description}\n# TODO: Implement {description}"
    
    def _generate_hello_world(self, language: str) -> str:
        """Generate Hello World program."""
        templates = {
            "python": 'print("Hello, World!")',
            "javascript": 'console.log("Hello, World!");',
            "java": '''public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}''',
            "cpp": '''#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}'''
        }
        return templates.get(language, "# Hello World template not available")
    
    def _generate_function(self, language: str) -> str:
        """Generate a simple function template."""
        templates = {
            "python": '''def my_function(param1, param2):
    """
    Function description here.
    """
    # Implementation here
    return param1 + param2''',
            "javascript": '''function myFunction(param1, param2) {
    // Function description here
    // Implementation here
    return param1 + param2;
}''',
            "java": '''public int myFunction(int param1, int param2) {
    // Function description here
    // Implementation here
    return param1 + param2;
}''',
            "cpp": '''int myFunction(int param1, int param2) {
    // Function description here
    // Implementation here
    return param1 + param2;
}'''
        }
        return templates.get(language, "# Function template not available")
    
    def _generate_class(self, language: str) -> str:
        """Generate a simple class template."""
        templates = {
            "python": '''class MyClass:
    """
    Class description here.
    """
    
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"''',
            "javascript": '''class MyClass {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}!`;
    }
}''',
            "java": '''public class MyClass {
    private String name;
    
    public MyClass(String name) {
        this.name = name;
    }
    
    public String greet() {
        return "Hello, " + name + "!";
    }
}''',
            "cpp": '''class MyClass {
private:
    std::string name;
    
public:
    MyClass(std::string n) : name(n) {}
    
    std::string greet() {
        return "Hello, " + name + "!";
    }
};'''
        }
        return templates.get(language, "# Class template not available")
    
    def help(self) -> str:
        """
        Return help information about the agent.
        Restituisce informazioni di aiuto sull'agente.
        """
        return f"""
{self.name} - Coding Agent / Agente di Codifica

Capabilities / Capacità:
1. analyze_file(filepath) - Analyze code files / Analizza file di codice
2. generate_code(description, language) - Generate code / Genera codice
3. help() - Show this help / Mostra questo aiuto

Supported languages / Linguaggi supportati: {', '.join(self.supported_languages)}

Example usage / Esempio di utilizzo:
    agent = CodingAgent()
    analysis = agent.analyze_file("example.py")
    code = agent.generate_code("hello world", "python")
"""


if __name__ == "__main__":
    # Example usage / Esempio di utilizzo
    print("=== Coding Agent Example / Esempio di Coding Agent ===\n")
    
    agent = CodingAgent("HAMong Assistant")
    
    # Show help
    print(agent.help())
    
    # Generate some example code
    print("\n=== Generating Hello World (Python) ===")
    hello_world = agent.generate_code("hello world", "python")
    print(hello_world)
    
    print("\n=== Generating a Function (JavaScript) ===")
    function = agent.generate_code("function", "javascript")
    print(function)
    
    print("\n=== Generating a Class (Python) ===")
    class_code = agent.generate_code("class", "python")
    print(class_code)
    
    # Create a test file and analyze it
    print("\n=== Analyzing this file ===")
    analysis = agent.analyze_file(__file__)
    print(f"File: {analysis['filename']}")
    print(f"Lines: {analysis['line_count']}")
    print(f"Functions: {analysis['functions']}")
    print(f"Has comments: {analysis['has_comments']}")
    print(f"Suggestions:")
    for suggestion in analysis['suggestions']:
        print(f"  - {suggestion}")
