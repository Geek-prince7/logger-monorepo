# Adding New Services

This monorepo uses Git submodules to manage microservices. Each service in `/services/` is an independent Git repository.

## Add a New Service

### 1. Create a Remote Repository
Create a new repository on GitHub/GitLab for your service.

### 2. Add as Submodule
```bash
# From the monorepo root
git submodule add <remote-url> services/<service-name>
git commit -m "Add <service-name> as submodule"
```

### 3. If Service Already Exists Locally
```bash
cd services/<service-name>
git init
git add .
git commit -m "Initial commit"
git remote add origin <remote-url>
git push -u origin main

# Return to monorepo root and add as submodule
cd ../..
git submodule add <remote-url> services/<service-name>
```

---

## Working with Submodules

### Clone Monorepo with All Services
```bash
git clone --recurse-submodules <monorepo-url>
```

### Pull Updates for All Services
```bash
git submodule update --remote --merge
```

### Work on a Specific Service
```bash
cd services/<service-name>
git checkout -b feature-branch
# make changes
git add . && git commit -m "Changes"
git push origin feature-branch
```

### Update Monorepo to Track New Service Commits
```bash
# After changes in a service are pushed
cd services/<service-name>
git pull origin main

# Return to root and commit the submodule pointer update
cd ../..
git add services/<service-name>
git commit -m "Update <service-name> to latest"
```

---

## Current Services

| Service | Repository |
|---------|------------|
| log-cdn | https://github.com/Geek-prince7/log-cdn.git |
| node-logger-sdk | https://github.com/Geek-prince7/node-sdk-log-collector.git |
