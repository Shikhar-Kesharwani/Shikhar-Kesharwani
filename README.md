<!-- Header -->
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=0,2,2,5,30&height=220&section=header&text=Ayush%20Gupta&fontSize=52&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Data%20Engineer%20%7C%20ML%20Developer%20%7C%20Full-Stack%20Builder&descAlignY=58&descSize=17" width="100%"/>
</div>

<!-- Typing SVG -->
<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=800&color=58A6FF&center=true&vCenter=true&multiline=false&random=false&width=700&lines=Building+Real+Systems+with+Real+Data+%F0%9F%9B%A0%EF%B8%8F;Delhi+NCR+Urban+Intelligence+Platform+%F0%9F%8F%99%EF%B8%8F;ML+%7C+Data+Engineering+%7C+FastAPI+%7C+RAG+%F0%9F%A4%96;No+Synthetic+Shortcuts.+Ever.+%E2%9C%85;B.Tech+CSE+%40+Bennett+University+%7C+Placements+2026+%F0%9F%8E%AF)](https://git.io/typing-svg)

</div>

<!-- Badges row -->
<div align="center">
  <img src="https://komarev.com/ghpvc/?username=AyushGU12&label=Profile+Views&color=0e75b6&style=flat-square" alt="profile views"/>
  &nbsp;
  <img src="https://img.shields.io/github/followers/AyushGU12?label=Followers&style=flat-square&color=0e75b6" alt="followers"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Focus-Data+Engineering+%7C+ML-brightgreen?style=flat-square" alt="focus"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Open%20To-Internships%20%26%20FTE-blue?style=flat-square" alt="open"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Real%20Data-Only-orange?style=flat-square" alt="real data"/>
</div>

<br/>

---

## 🧠 About Me

```python
class AyushGupta:
    def __init__(self):
        self.name        = "Ayush Gupta"
        self.role        = "Data Engineer | ML Developer | Full-Stack Builder"
        self.university  = "Bennett University, Greater Noida"
        self.location    = "Greater Noida, UP, India 📍"
        self.focus       = ["Data Engineering Pipelines", "ML Systems", "Urban Analytics"]
        self.building    = "Delhi NCR Urban Intelligence Platform — 52 localities, 6 domains"
        self.principle   = "Real data only. No synthetic shortcuts. Ever."
        self.target      = "SDE / MLE Placements 2026 🎯"
        self.fun_fact    = "I write ETL pipelines at 2am and call it debugging 🌙"

    def stack(self):
        return {
            "languages":    ["Python", "C++", "Java", "SQL"],
            "data_eng":     ["Pandas", "NumPy", "ohsome API", "OpenStreetMap ETL"],
            "ml":           ["Scikit-learn", "XGBoost", "CNN", "Random Forest", "ONNX"],
            "backends":     ["FastAPI", "Streamlit"],
            "databases":    ["SQLite", "PostgreSQL", "ChromaDB"],
            "devops":       ["Docker", "Git", "GitHub Actions", "AWS EC2/S3"],
            "ai":           ["LangChain", "RAG", "Grad-CAM", "Text-to-SQL"],
        }

    def contact(self):
        return {
            "email":  "ayushgu02@gmail.com",
            "github": "github.com/AyushGU12",
        }

    def __str__(self):
        return "Engineer who ships systems that work on real data in production."

me = AyushGupta()
print(me)
# Output: Engineer who ships systems that work on real data in production.
```

---

## 🚀 Featured Projects

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3>🏙️ Delhi NCR Urban Intelligence Platform</h3>
      <p>
        Development analytics across 52 NCR localities spanning Delhi, Noida, Greater Noida,
        Gurgaon, Faridabad, Ghaziabad — 6 domains (health, education, transport, environment,
        commercial, governance). Full ohsome API + RBI DBIE ETL pipeline with 16-year coverage
        (2011–2026). Zero nulls. Zero synthetic data. Per-10k ratios, catchment analysis at
        500m/1km/2km radii, year-on-year drift detection.
      </p>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white"/>
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
        <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"/>
        <img src="https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white"/>
      </p>
      <details>
        <summary>💡 What I learned building this</summary>
        <ul>
          <li>ohsome API polygon querying at scale with rate-limit backoff strategies</li>
          <li>Incremental ETL with staging DB swap to avoid corrupt production state</li>
          <li>Catchment-radius spatial joins using GeoPandas for multi-ring analysis</li>
          <li>RBI DBIE API pagination and fiscal-year alignment with calendar data</li>
        </ul>
      </details>
      <a href="https://github.com/AyushGU12">
        <img src="https://img.shields.io/badge/View%20Repo-%23181717?style=flat-square&logo=github&logoColor=white"/>
      </a>
    </td>
    <td width="50%" valign="top">
      <h3>🌾 Crop Recommendation System</h3>
      <p>
        Random Forest classifier on 7 soil/climate inputs (N, P, K, pH, humidity, rainfall,
        temperature) returning top-3 crop recommendations with confidence scores. Geographic
        exclusion filtering prevents climatically impossible suggestions. Deployed via FastAPI
        with Streamlit UI. 97%+ accuracy on validation set.
      </p>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
        <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>
        <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
      </p>
      <details>
        <summary>💡 What I learned building this</summary>
        <ul>
          <li>Geographic exclusion via lookup table beats model-level constraints for explainability</li>
          <li>Confidence calibration: raw RF probabilities vs. Platt scaling tradeoffs</li>
          <li>Top-k output design for agri-advisory UX vs. single prediction systems</li>
        </ul>
      </details>
      <a href="https://github.com/AyushGU12">
        <img src="https://img.shields.io/badge/View%20Repo-%23181717?style=flat-square&logo=github&logoColor=white"/>
      </a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🌿 Crop Disease Detection Platform</h3>
      <p>
        CNN-from-scratch architecture (no pretrained weights) for plant disease classification.
        ONNX export for cross-platform inference. FastAPI backend with Grad-CAM visualization
        overlay — shows <em>which leaf regions</em> triggered the prediction. Designed for
        deployment on low-resource edge devices in agricultural settings.
      </p>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>
        <img src="https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white"/>
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
        <img src="https://img.shields.io/badge/GradCAM-FF6B35?style=flat-square"/>
      </p>
      <details>
        <summary>💡 What I learned building this</summary>
        <ul>
          <li>Building CNN blocks from scratch forces understanding of receptive fields and gradient flow</li>
          <li>ONNX export graph tracing pitfalls with dynamic input shapes</li>
          <li>Grad-CAM: hooking into intermediate activations without modifying architecture</li>
        </ul>
      </details>
      <a href="https://github.com/AyushGU12">
        <img src="https://img.shields.io/badge/View%20Repo-%23181717?style=flat-square&logo=github&logoColor=white"/>
      </a>
    </td>
    <td width="50%" valign="top">
      <h3>🌐 DNS Resolver — From Scratch</h3>
      <p>
        Pure Python DNS resolver with zero library dependencies. Walks the full DNS hierarchy:
        Root → TLD → Authoritative. Implements DNS compression pointer decoding, CNAME chain
        resolution, in-memory TTL cache, and A/NS/CNAME/AAAA record support. 13 hardcoded
        root servers. Manual byte-level packet parsing over raw UDP sockets.
      </p>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/UDP%2FTCP-00599C?style=flat-square&logoColor=white"/>
        <img src="https://img.shields.io/badge/No%20Libraries-success?style=flat-square"/>
        <img src="https://img.shields.io/badge/Networking-FF6B35?style=flat-square"/>
      </p>
      <details>
        <summary>💡 What I learned building this</summary>
        <ul>
          <li>DNS wire format: label encoding, compression pointer offset arithmetic</li>
          <li>Iterative vs. recursive resolution — why resolvers use iterative in practice</li>
          <li>TTL cache invalidation and negative caching (NXDOMAIN) edge cases</li>
        </ul>
      </details>
      <a href="https://github.com/AyushGU12">
        <img src="https://img.shields.io/badge/View%20Repo-%23181717?style=flat-square&logo=github&logoColor=white"/>
      </a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>💬 Text-to-SQL with Hallucination Detection</h3>
      <p>
        Natural language → SQL interface with LLM-as-judge verification layer. Detects
        column hallucinations, schema drift, and invalid JOIN paths before query execution.
        Supports multi-table schemas with FK relationships. Differentiator: confidence
        scoring per clause, not just pass/fail query validation.
      </p>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>
        <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"/>
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
      </p>
      <a href="https://github.com/AyushGU12">
        <img src="https://img.shields.io/badge/View%20Repo-%23181717?style=flat-square&logo=github&logoColor=white"/>
      </a>
    </td>
    <td width="50%" valign="top">
      <h3>❤️ CardioSense / ChestVision AI</h3>
      <p>
        Healthcare ML platform for cardiac risk stratification and chest X-ray pathology
        detection. Gradient-boosted ensemble on clinical tabular features; CNN classifier
        for X-ray abnormality localisation. Sehat — a unified healthcare portal integrating
        both inference modules with patient-facing explanation outputs.
      </p>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/XGBoost-EA4335?style=flat-square"/>
        <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
      </p>
      <a href="https://github.com/AyushGU12">
        <img src="https://img.shields.io/badge/View%20Repo-%23181717?style=flat-square&logo=github&logoColor=white"/>
      </a>
    </td>
  </tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

### 🤖 AI / Machine Learning
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EA4335?style=for-the-badge&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![ONNX](https://img.shields.io/badge/ONNX-005CED?style=for-the-badge&logo=onnx&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

### 🗄️ Data Engineering
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=for-the-badge&logo=openstreetmap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B35?style=for-the-badge&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=white)

### ⚙️ Frameworks & APIs
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

### 💻 Languages
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

### 🚀 DevOps & Cloud
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

</div>

---

## 📊 GitHub Stats

<div align="center">
  <img width="49%" src="https://github-readme-stats.vercel.app/api?username=AyushGU12&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&include_all_commits=true&rank_icon=github" />
  <img width="49%" src="https://github-readme-streak-stats.herokuapp.com/?user=AyushGU12&theme=tokyonight&hide_border=true" />
</div>

<div align="center">
  <img width="42%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=AyushGU12&layout=donut&theme=tokyonight&hide_border=true&langs_count=8" />
</div>

---

## 🏆 Trophies

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=AyushGU12&theme=tokyonight&no-frame=true&no-bg=true&margin-w=6&column=7" />
</div>

---

## 📈 Contribution Activity

<div align="center">
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=AyushGU12&bg_color=1a1b27&color=70a5fd&line=bf91f3&point=38bdae&area=true&hide_border=true&area_color=bf91f3" />
</div>

---

## 🎯 Current Focus

<table>
  <tr>
    <td>🔨 Building</td>
    <td>Delhi NCR Urban Intelligence Platform — 52 localities, strict real-data pipeline</td>
  </tr>
  <tr>
    <td>🔨 Building</td>
    <td>Text-to-SQL interface with per-clause hallucination detection</td>
  </tr>
  <tr>
    <td>📚 Learning</td>
    <td>Corrective RAG · LangGraph Agents · Spatial SQL · DNS internals</td>
  </tr>
  <tr>
    <td>🎯 Target</td>
    <td>SDE / MLE Placements 2026 — Data Engineering & AI/ML roles</td>
  </tr>
  <tr>
    <td>🌍 Domains</td>
    <td>Urban Analytics · Indian Agriculture · Healthcare AI · NLP</td>
  </tr>
  <tr>
    <td>📍 Location</td>
    <td>Greater Noida, Uttar Pradesh, India</td>
  </tr>
</table>

---

## 📚 Currently Exploring

> Things I'm reading, researching, or experimenting with this month

- **Spatial data engineering** — PostGIS, H3 hexagonal indexing for urban density analysis
- **RAG architecture patterns** — Corrective RAG, Self-RAG, hybrid BM25+dense retrieval
- **Systems programming** — how DNS, TCP, and HTTP are actually implemented at the byte level
- **Interview prep** — OS (virtual memory, scheduling), CN (TCP congestion, routing), DBMS (B-trees, ACID)

---

## 💡 My Engineering Principle

<div align="center">

> **"Real data only. No synthetic shortcuts."**
>
> Every project uses verified, authentic datasets —
> OpenStreetMap, RBI DBIE, ICRISAT, NASA POWER, data.gov.in Agmarknet.
> If the data doesn't exist, I document the gap honestly
> rather than fabricate numbers to make the dashboard look nice.

</div>

---

## 🤝 Let's Build Something

<div align="center">

**Open to internships, FTE roles, hackathon collabs, and open-source contributions**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AyushGU12)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ayushgu02@gmail.com)

</div>

---

## 😂 Random Dev Joke

<div align="center">
  <img src="https://readme-jokes.vercel.app/api?theme=tokyonight&hideBorder" alt="dev joke" />
</div>

---

<!-- Snake animation -->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AyushGU12/AyushGU12/blob/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/AyushGU12/AyushGU12/blob/output/github-contribution-grid-snake.svg" />
    <img alt="snake animation" src="https://github.com/AyushGU12/AyushGU12/blob/output/github-contribution-grid-snake-dark.svg" />
  </picture>
</div>

<!-- Footer -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,5,30&height=100&section=footer" width="100%"/>
</div>
