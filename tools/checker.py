import os,re

def check(path,data):
    files=data["files"]
    text="\n".join(x[1] for x in data["source"])
    findings=[]
    category="TestMedic"

    if not files:
        findings.append({
            "problem":"No detectable project files were found.",
            "cause":"The inspected directory appears empty.",
            "evidence":"The scanner detected no files.",
            "suggested_fix":"Provide the relevant project files.",
            "confidence":"high"
        })

    rules={
      "TestMedic":(not any("test" in f.lower() or "spec" in f.lower() for f in files),"No recognizable test file was detected.","Add automated tests."),
      "DependencyMedic":(not any(os.path.basename(f).lower() in {"package.json","requirements.txt","pyproject.toml","pom.xml","build.gradle"} for f in files),"No dependency manifest was detected.","Add or verify the dependency manifest."),
      "SecurityMedic":(bool(re.search(r'(password|secret|api[_-]?key)\s*[:=]\s*["\'][^"\']{6,}',text,re.I)),"Possible hard-coded credential pattern detected.","Move credentials to secure secret management."),
      "LogMedic":(not any("log" in f.lower() for f in files),"No recognizable log file was detected.","Provide structured application logs."),
      "ConfigMedic":(not any(os.path.basename(f).lower() in {".env.example","config.json","config.yaml","config.yml"} for f in files),"No recognizable configuration example was detected.","Add a safe example configuration."),
      "GitMedic":(".gitignore" not in [os.path.basename(f) for f in files],"No .gitignore file was detected.","Add a .gitignore."),
      "IssueMedic":(not any("issue" in f.lower() or "template" in f.lower() for f in files),"No issue-management template was detected.","Add issue templates or guidance."),
      "PRMedic":(not any("contribut" in f.lower() or "pull_request" in f.lower() for f in files),"No contribution or PR guidance was detected.","Add contribution and pull-request guidance."),
      "SQLMedic":(bool(re.search(r"select\s+\*\s+from",text,re.I)),"Wildcard SQL query detected.","Select only required columns."),
      "CodeMedic":(bool(re.search(r"console\.log\s*\(|print\s*\(\s*['\"]debug",text,re.I)),"Debug output pattern detected.","Remove or replace debug output."),
      "DeployMedic":(not any(os.path.basename(f).lower() in {"dockerfile","vercel.json","render.yaml","fly.toml"} for f in files),"No recognizable deployment configuration was detected.","Add deployment configuration if required."),
      "CloudMedic":(not any("terraform" in f.lower() or "cloudformation" in f.lower() for f in files),"No recognizable cloud infrastructure configuration was detected.","Add infrastructure configuration if applicable."),
      "PackageMedic":(not any(os.path.basename(f).lower() in {"package.json","pyproject.toml","pom.xml"} for f in files),"No package metadata file was detected.","Add the appropriate project manifest."),
      "PerformanceMedic":(bool(re.search(r"for\s*\([^\n]+\)\s*\{[\s\S]{0,300}for\s*\(",text)),"Potential nested-loop pattern detected.","Review nested iteration."),
      "EnvMedic":(bool(re.search(r"os\.getenv|process\.env",text)) and not any(".env.example" in f.lower() for f in files),"Environment variables are used without an example file.","Document required environment variables safely."),
      "DockerMedic":(not any(os.path.basename(f).lower()=="dockerfile" for f in files),"No Dockerfile was detected.","Add a Dockerfile if container deployment is intended."),
      "LicenseMedic":(not any(os.path.basename(f).lower().startswith("license") for f in files),"No license file was detected.","Add an appropriate license if applicable."),
      "StructureMedic":(len([f for f in files if os.path.dirname(f)==""])>12,"Many files are located directly in the project root.","Group related files into directories."),
      "APIDocMedic":(bool(re.search(r"\.(get|post|put|patch|delete)\s*\(",text,re.I)) and not any("openapi" in f.lower() or "swagger" in f.lower() for f in files),"API routes were detected without API documentation.","Add OpenAPI or Swagger documentation."),
      "MigrationMedic":(len([f for f in files if "migration" in f.lower()])>1 and len(set(re.findall(r"\d{3,}", "\n".join(files))))<len([f for f in files if "migration" in f.lower()]),"Duplicate migration version numbers may exist.","Review migration ordering and unique versions.")
    }

    if category in rules:
        hit,msg,fix=rules[category]
        if hit:
            findings.append({"problem":msg,"cause":"Project evidence matched a diagnostic rule.","evidence":"The scanner detected a matching pattern.","suggested_fix":fix,"confidence":"high"})

    return {"status":"healthy","message":"No known problems were detected."} if not findings else {"status":"problems_detected","findings":findings}
