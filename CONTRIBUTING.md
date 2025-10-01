# Contributing to Nitinol Phase Visualization

Thank you for your interest in contributing to this educational project! We welcome contributions from developers, educators, scientists, and anyone passionate about making materials science accessible to kids and students.

## How Can You Contribute?

### 🐛 Bug Reports
Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Your Python version and OS

### 💡 Feature Requests
Have an idea? We'd love to hear it! Please include:
- What problem does it solve?
- Who would benefit (kids, teachers, researchers)?
- How should it work?
- Any reference materials or examples

### 🎓 Educational Content
- Lesson plans for classroom use
- Science experiment guides
- Documentation improvements
- Tutorial videos or blog posts

### 💻 Code Contributions

#### Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/nitinol-phase-visualization.git
   cd nitinol-phase-visualization
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install ase matplotlib numpy
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Code Standards

- **Python Style**: Follow PEP 8 guidelines
- **Comments**: Include clear docstrings for functions and classes
- **Educational Focus**: Keep code readable for students learning Python
- **Testing**: Test your changes with different parameter configurations

#### Example Code Structure

```python
def create_new_visualization(param1, param2):
    """
    Brief description of what this function does

    Parameters:
    -----------
    param1 : type
        Description
    param2 : type
        Description

    Returns:
    --------
    result : type
        Description
    """
    # Implementation
    pass
```

### 📚 Documentation

- Fix typos or unclear explanations
- Add examples and use cases
- Translate documentation to other languages
- Create video tutorials or blog posts

### 🎨 Design and Visualization

- Improve color schemes for accessibility
- Create better default viewing angles
- Design educational posters or infographics
- Enhance UI/UX for kid-friendly interaction

## Development Guidelines

### Adding New Features

1. **Discuss First**: Open an issue to discuss major changes before implementing
2. **Keep It Educational**: Remember the target audience (kids, students, educators)
3. **Maintain Compatibility**: Ensure changes work with existing parameters
4. **Document**: Update README.md and add code comments
5. **Test**: Verify the visualization renders correctly

### Crystal Structure Accuracy

When adding new phases or structures:
- Reference peer-reviewed literature
- Include citations in code comments
- Validate lattice parameters
- Test with known experimental data

### Performance Considerations

- Keep atom counts reasonable (< 200 atoms for smooth interaction)
- Optimize rendering for real-time rotation
- Test on different hardware configurations

## Submission Process

1. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

2. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Include screenshots for visual changes
   - Explain educational benefits

4. **Code Review**
   - Respond to feedback constructively
   - Make requested changes
   - Keep the discussion focused and professional

## Pull Request Checklist

- [ ] Code follows PEP 8 style guidelines
- [ ] Functions have clear docstrings
- [ ] Changes are tested and working
- [ ] Documentation updated (README, comments)
- [ ] No breaking changes to existing functionality
- [ ] Educational value clearly explained
- [ ] Screenshots included (for visual changes)

## Ideas for Contributions

### High Priority
- [ ] Add R-phase intermediate structure visualization
- [ ] Implement temperature slider to show phase transitions
- [ ] Create animated transformation between phases
- [ ] Add export to STL for 3D printing
- [ ] Develop lesson plan templates for teachers

### Educational Enhancements
- [ ] Interactive quiz mode about crystal structures
- [ ] Augmented reality (AR) visualization for mobile
- [ ] Virtual reality (VR) support for immersive learning
- [ ] Atom-labeling mode for identifying specific atoms
- [ ] Comparison with other shape-memory alloys

### Technical Improvements
- [ ] Unit tests for structure generation
- [ ] Performance optimization for larger structures
- [ ] Command-line interface with more options
- [ ] Web-based version using Python to JavaScript
- [ ] Integration with Jupyter notebooks

### Documentation & Outreach
- [ ] Video tutorials for YouTube
- [ ] Blog posts about shape-memory alloys
- [ ] Science fair project templates
- [ ] Translations to other languages
- [ ] Accessibility improvements

## Community Guidelines

### Be Respectful
- Welcome newcomers and beginners
- Provide constructive feedback
- Assume good intentions
- Be patient with questions

### Educational Mission
Remember this project's goal: making materials science accessible and exciting for kids and students. Keep contributions:
- **Simple**: Easy to understand and use
- **Visual**: Engaging and interactive
- **Accurate**: Scientifically correct
- **Fun**: Enjoyable to explore

### Attribution
- Give credit where it's due
- Cite scientific sources
- Acknowledge contributors
- Respect intellectual property

## Getting Help

- **Questions?** Open a GitHub issue with the "question" label
- **Stuck?** Describe what you've tried and where you're blocked
- **Ideas?** Start a discussion in GitHub Discussions
- **Security Issues?** Email privately (don't open public issue)

## Recognition

Contributors will be:
- Listed in the project README
- Acknowledged in release notes
- Credited in any publications using this code
- Part of making science education better!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for helping make materials science education more accessible and exciting for kids around the world! 🔬✨**

*Every contribution, no matter how small, makes a difference in inspiring the next generation of scientists and engineers.*
