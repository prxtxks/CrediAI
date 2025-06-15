#!/usr/bin/env bash
set -euo pipefail

BASE="/Users/pratik/Github_Projects/CrediAI"

echo "Creating project skeleton at: $BASE"

# Ensure base dir exists
if [ ! -d "$BASE" ]; then
  echo "Error: base directory does not exist: $BASE"
  echo "Create or clone your repo at that path first."
  exit 1
fi

cd "$BASE"

# Helper to create dirs and files
mkf() {
  local dirpath="$1"
  local file="$2"
  mkdir -p "$dirpath"
  if [ ! -f "$dirpath/$file" ]; then
    # put small header based on extension
    case "$file" in
      *.py) echo "# auto-generated placeholder: $file" > "$dirpath/$file" ;;
      *.sh) echo "#!/usr/bin/env bash" > "$dirpath/$file"; chmod +x "$dirpath/$file" ;;
      *.md) echo "# $file" > "$dirpath/$file" ;;
      *.json) echo "{}" > "$dirpath/$file" ;;
      *.yml|*.yaml) echo "# $file" > "$dirpath/$file" ;;
      *.sql) echo "-- $file" > "$dirpath/$file" ;;
      *.js) echo "// placeholder $file" > "$dirpath/$file" ;;
      *.jsx) echo "// placeholder $file" > "$dirpath/$file" ;;
      *.css) echo "/* placeholder $file */" > "$dirpath/$file" ;;
      *.html) echo "<!-- placeholder $file -->" > "$dirpath/$file" ;;
      *) touch "$dirpath/$file" ;;
    esac
    echo "created: $dirpath/$file"
  else
    echo "exists:  $dirpath/$file"
  fi
}

# Start creating structure
# backend/app/api
mkf backend/app/api __init__.py
mkf backend/app/api auth.py
mkf backend/app/api predict.py
mkf backend/app/api train.py
mkf backend/app/api users.py
mkf backend/app/api health.py
mkf backend/app/api loans.py

# backend core
mkf backend/app/core __init__.py
mkf backend/app/core config.py
mkf backend/app/core security.py
mkf backend/app/core logging_config.py

# backend database
mkf backend/app/database __init__.py
mkf backend/app/database connection.py
mkf backend/app/database models.py
mkf backend/app/database seed_data.sql

# backend ml
mkf backend/app/ml __init__.py
mkf backend/app/ml preprocess.py
mkf backend/app/ml train_model.py
mkf backend/app/ml predict_model.py
mkf backend/app/ml feature_engineering.py
mkf backend/app/ml metrics.py
mkdir -p backend/app/ml/saved_models
if [ ! -f backend/app/ml/saved_models/placeholder.txt ]; then echo "placeholder" > backend/app/ml/saved_models/placeholder.txt; fi
echo "created: backend/app/ml/saved_models/placeholder.txt"

# backend schemas
mkf backend/app/schemas __init__.py
mkf backend/app/schemas user_schemas.py
mkf backend/app/schemas loan_schemas.py
mkf backend/app/schemas predict_schemas.py

# backend utils
mkf backend/app/utils __init__.py
mkf backend/app/utils jwt_utils.py
mkf backend/app/utils hashing.py
mkf backend/app/utils exceptions.py

# backend main
mkf backend/app main.py
mkf backend/app __init__.py

# backend tests
mkf backend/tests test_auth.py
mkf backend/tests test_predict.py
mkf backend/tests test_loans.py

# backend top-level files
mkf backend "" requirements.txt
mkf backend "" Dockerfile
mkf backend "" README.md

# database dir
mkf database "" init.sql
mkf database "" create_tables.sql
mkf database "" seed.sql
mkf database "" Dockerfile

# frontend structure
mkdir -p frontend/src/components
mkdir -p frontend/src/pages
mkdir -p frontend/src/assets
touch frontend/public/favicon.ico || true

# frontend components
mkf frontend/src/components Navbar.jsx
mkf frontend/src/components Footer.jsx
mkf frontend/src/components LoanForm.jsx
mkf frontend/src/components PredictionResult.jsx
mkf frontend/src/components AdminSidebar.jsx
mkf frontend/src/components UserCard.jsx

# frontend pages
mkf frontend/src/pages Home.jsx
mkf frontend/src/pages Login.jsx
mkf frontend/src/pages Dashboard.jsx
mkf frontend/src/pages Applications.jsx
mkf frontend/src/pages Predictions.jsx

# frontend src root
mkf frontend/src App.jsx
mkf frontend/src main.jsx
mkf frontend/src index.css

# frontend configs
mkf frontend "" vite.config.js
mkf frontend "" package.json
mkf frontend "" tailwind.config.js
mkf frontend "" postcss.config.js
mkf frontend "" Dockerfile

# root level files
mkf . "" docker-compose.yml
mkf . "" .env
mkf . "" .gitignore
mkf . "" README.md

# Ensure executable bits for shell files (if any)
if [ -f "create_structure.sh" ]; then chmod +x create_structure.sh; fi

echo ""
echo "✅ Project skeleton created under: $BASE"
echo "Next steps:"
echo "  1) cd $BASE"
echo "  2) git add . && git commit -m 'add skeleton' (optional)"
echo "  3) Ask me which file you want implemented first, e.g., backend/app/api/predict.py" 