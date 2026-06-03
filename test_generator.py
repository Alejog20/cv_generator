import os
import pytest
from generator import generate_pdf, sanitize

# 1. A "Fixture" provides reusable dummy data for our tests
@pytest.fixture
def sample_cv_data():
    return {
        "name": "Jane Doe",
        "title": "Software Engineer",
        "email": "jane@example.com",
        "phone": "555-0100",
        "summary": "A passionate developer.",
        "skills": ["Python", "Typst", "Git"],
        "projects": [{"Name": "Test Project", "Link": "github.com/test", "Description": "A test project."}]
    }

# 2. Test our sanitization function
def test_sanitize_removes_dangerous_characters():
    # It should escape the brackets
    assert sanitize("<ironmountain.com>") == r"\<ironmountain.com\>"
    # It should handle empty or non-string inputs safely
    assert sanitize(None) == ""
    assert sanitize(123) == ""

# 3. Test successful PDF generation
def test_generate_pdf_success(sample_cv_data, tmp_path):
    # tmp_path is a brilliant Pytest feature that creates a temporary folder just for this test
    output_file = str(tmp_path / "test_cv.pdf")
    
    success, result = generate_pdf(sample_cv_data, output_filename=output_file)
    
    # By adding the result to the assert, Pytest will print the exact Typst error if it fails!
    assert success is True, f"PDF Generation failed with error: {result}"
    assert os.path.exists(result), "The PDF file was not found on the disk."
    assert result.endswith(".pdf"), "The output does not have a PDF extension."

# 4. Test edge case: Missing data
def test_generate_pdf_with_empty_data(tmp_path):
    output_file = str(tmp_path / "empty_cv.pdf")
    
    # Passing an empty dictionary should NOT crash the compiler
    success, result = generate_pdf({}, output_filename=output_file)
    
    assert success is True
    assert os.path.exists(result), "The PDF failed to generate with empty data."
