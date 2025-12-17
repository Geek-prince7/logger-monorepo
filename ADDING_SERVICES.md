# Adding New Services as Submodules

This monorepo uses **Git submodules** to manage microservices. Each service in `/services/` is an independent Git repository with its own branching and versioning.

---

## Step-by-Step: Add a New Service

### Scenario A: Creating a Brand New Service

**Step 1:** Create your service folder and code
```bash
cd /Users/princedubey/projects/logkey/services
mkdir my-new-service
cd my-new-service
# Add your code files here
```

**Step 2:** Create a remote repository on GitHub
- Go to https://github.com/new
- Create a new empty repository (e.g., `my-new-service`)
- Copy the repo URL (e.g., `https://github.com/Geek-prince7/my-new-service.git`)

**Step 3:** Initialize Git and push to remote
```bash
cd /Users/princedubey/projects/logkey/services/my-new-service

git init
git add .
git commit -m "Initial commit - My New Service"
git remote add origin https://github.com/Geek-prince7/my-new-service.git
git branch -M main
git push -u origin main
```

**Step 4:** Register as submodule in the parent repo
```bash
cd /Users/princedubey/projects/logkey

git submodule add https://github.com/Geek-prince7/my-new-service.git services/my-new-service
git commit -m "Add my-new-service as submodule"
git push
```

---

### Scenario B: Service Already Has a Remote Repository

If the service repo already exists on GitHub:

```bash
cd /Users/princedubey/projects/logkey

git submodule add https://github.com/Geek-prince7/existing-service.git services/existing-service
git commit -m "Add existing-service as submodule"
git push
```

---

## Verify Submodule Setup

```bash
cd /Users/princedubey/projects/logkey

# Check all submodules
git submodule status

# Should show something like:
# ccdfbf9 services/log-cdn (heads/main)
# fd89af7 services/node-logger-sdk (heads/main)
# abc1234 services/my-new-service (heads/main)
```

---

## Working with Submodules

### Clone Monorepo with All Services
```bash
git clone --recurse-submodules https://github.com/Geek-prince7/logger-monorepo.git
```

### Update All Services to Latest
```bash
git submodule update --remote --merge
```

### Work on a Specific Service (Independent Branching)
```bash
cd services/my-new-service
git checkout -b feature/new-feature
# make changes
git add . && git commit -m "Add new feature"
git push origin feature/new-feature
```

### Update Monorepo After Service Changes
```bash
# After pushing changes in a service
cd /Users/princedubey/projects/logkey
git add services/my-new-service
git commit -m "Update my-new-service to latest"
git push
```

---

## Current Services

| Service | Repository |
|---------|------------|
| log-cdn | https://github.com/Geek-prince7/log-cdn.git |
| node-logger-sdk | https://github.com/Geek-prince7/node-sdk-log-collector.git |

---

## Quick Reference Commands

| Action | Command |
|--------|---------|
| Add submodule | `git submodule add <url> services/<name>` |
| Clone with submodules | `git clone --recurse-submodules <url>` |
| Update all submodules | `git submodule update --remote --merge` |
| Check submodule status | `git submodule status` |
| Initialize submodules after clone | `git submodule update --init --recursive` |
