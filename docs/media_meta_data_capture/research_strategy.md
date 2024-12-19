To capture this work without committing code directly to the main repository, you can use a structured approach that keeps the project organized and allows for iterative experimentation. Here's how you can proceed:

----------

### **1. Create a Separate Experimental Branch**

-   Create a new branch in your repository specifically for this evaluation task:
    
    ```bash
    git checkout -b feature/video-metadata-evaluation
    
    ```
    
-   Work on this branch without affecting the main project.

----------

### **2. Set Up a Dedicated Directory for Prototyping**

-   In your branch, create a subdirectory for experimentation:
    
    ```
    project-root/
    ├── experiments/
    │   ├── metadata_extraction/
    │   │   ├── ffmpeg_test.py
    │   │   ├── moviepy_test.py
    │   │   ├── pymediainfo_test.py
    │   │   └── README.md
    
    ```
    
-   Use this directory to write and run evaluation scripts, keeping them separate from production code.

----------

### **3. Document Your Work**

-   Create a `README.md` in the `metadata_extraction/` directory to document:
    -   Purpose of the experiments.
    -   Results from testing the libraries.
    -   Code snippets for each library.
    -   Observations and recommendations.
-   Use Markdown for formatting and tables to summarize findings.

Example snippet for the `README.md`:

```markdown
# Video Metadata Extraction Evaluation

## Purpose
Evaluate `ffmpeg-python`, `moviepy`, and `pymediainfo` for extracting video metadata.

## Tested Fields
- Duration
- Resolution (width x height)
- Codec type
- File size

## Summary Table

| Library         | Duration | Resolution | Codec Type | File Size | Ease of Use | Dependencies      |
|------------------|----------|------------|------------|-----------|-------------|-------------------|
| `ffmpeg-python` | ✅       | ✅         | ✅         | ✅        | Moderate    | FFmpeg CLI        |
| `moviepy`       | ✅       | ✅         | ❌         | ❌        | Easy        | None              |
| `pymediainfo`   | ✅       | ✅         | ✅         | ✅        | Moderate    | MediaInfo CLI     |

## Recommendations
- **Primary Choice**: Use `ffmpeg-python` for its comprehensive metadata and integration potential.
- **Alternative**: Consider `pymediainfo` if CLI dependencies are acceptable.
- Avoid `moviepy` for detailed metadata extraction due to its limited support.

```

----------

### **4. Capture Research in GitHub Issues or a Wiki**

-   **GitHub Issues**: Write a summary of your findings in the relevant GitHub issue for video metadata extraction.
-   **GitHub Wiki**: Add a wiki page to document the evaluation process and results.

Example issue comment:

```markdown
### Video Metadata Extraction Evaluation

#### Tested Libraries
1. `ffmpeg-python`
2. `moviepy`
3. `pymediainfo`

#### Summary of Findings
- `ffmpeg-python` is the most feature-complete for metadata extraction.
- `moviepy` is simple to use but lacks support for key metadata fields.
- `pymediainfo` provides robust metadata but requires MediaInfo CLI dependencies.

#### Recommendations
- Proceed with `ffmpeg-python` for integration with the Media Scan application.
- See the `experiments/metadata_extraction/` directory for prototype scripts and detailed evaluation notes.

```

----------

### **5. Push and Share the Branch**

-   Push the branch to the repository for visibility:
    
    ```bash
    git push origin feature/video-metadata-evaluation
    
    ```
    
-   Invite collaborators (if any) to review or contribute to the experiments.

----------

### **6. Finalize Decisions**

-   Once the evaluation is complete, make a decision on the library to use.
-   Archive or remove the `experiments/` directory before merging the branch into the main project.
-   Commit only the necessary integration code to the production repository.

Let me know if you'd like templates for the `README.md` or GitHub issue comments!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg2MDc0Mzg5NF19
-->