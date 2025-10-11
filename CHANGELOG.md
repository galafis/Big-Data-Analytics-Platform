# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-10-11

### Added
- Comprehensive troubleshooting guide (`TROUBLESHOOTING.md`)
  - Git branch error documentation and solutions
  - Dynamic branch detection examples
  - Common issues and solutions
- Branch helper utility script (`scripts/branch-helper.sh`)
  - Automatic default branch detection
  - Branch existence checking
  - Branch comparison functionality
  - Repository information display
- Enhanced README.md with Git branch troubleshooting
  - Added `refs/heads/master` error solution in both languages
  - Updated project structure to include new files
  - References to comprehensive troubleshooting guide
- Updated CONTRIBUTING.md with branch structure guidelines
  - Documented use of `main` as default branch
  - Added workflow for creating branches
  - Reference to troubleshooting guide

### Fixed
- Addressed Git error: "fatal: ambiguous argument 'refs/heads/master': unknown revision or path not in the working tree"
- Provided multiple solutions for branch reference issues

## [2.0.0] - 2025-10-11

### Added
- Comprehensive README with bilingual content (PT-BR and EN)
- Table of contents for easy navigation
- Architecture diagrams showing data flow
- Usage examples with expected output
- Troubleshooting section with common issues
- Future enhancements roadmap
- Professional hero image from Unsplash
- Web dashboard preview with screenshot
- GitHub Actions workflow for automated testing (`.github/workflows/test.yml`)
- Comprehensive docstrings with type hints for all functions
- Input validation with descriptive error messages
- Robust error handling with user-friendly messages
- Enhanced test suite with edge cases and integration tests
- Modern web interface with gradient design
- Real-time statistics cards (categories, transactions, revenue, average sale)
- Sortable table columns
- Responsive design for mobile and desktop
- Loading states and error handling in web interface
- Currency and number formatting
- Comprehensive audit report (`AUDIT_REPORT.md`)
- This changelog file

### Changed
- Fixed typo: "Eletronics" → "Electronics" in `data_processor.py`
- Fixed README.md formatting: missing `**` closing tag
- Fixed README.md: Portuguese text in English section
- Enhanced `.gitignore` with Python cache, generated files, IDE and OS files
- Improved test messages with descriptive assertions
- Modernized web interface design with better UX
- Enhanced CSS with modern styling and responsiveness
- Updated web interface to show statistics and improved table

### Removed
- Duplicate `README_content.md` file
- Placeholder image references
- Python cache files (`__pycache__/`) from repository
- Generated CSV files from repository (now properly gitignored)

### Fixed
- Code typo causing inconsistent category names
- README formatting issues
- Missing closing tags in markdown
- Language inconsistencies in documentation
- Missing input validation in data processing functions
- Lack of error handling
- Basic test coverage
- Repository hygiene issues (cache files, duplicates)

## [1.0.0] - 2023-XX-XX

### Added
- Initial project structure
- Basic data processor with dummy data generation
- Sales analysis by category functionality
- Simple unit tests
- Basic web interface
- README with project description
- MIT License
- Code of Conduct
- Contributing guidelines
- Python dependencies file

[2.0.0]: https://github.com/galafis/Big-Data-Analytics-Platform/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/galafis/Big-Data-Analytics-Platform/releases/tag/v1.0.0
