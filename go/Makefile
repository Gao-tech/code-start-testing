# build-GoFunction:
# 	@echo "🛠 Building Go Lambda..."
# 	GOOS=linux GOARCH=arm64 go build -o bootstrap main.go
# 	cp bootstrap $(ARTIFACTS_DIR)/  # SAM requires this copy
# 	@echo "✅ Built bootstrap binary"

build-GoFunction:
	@echo "🛠 Building Go Lambda..."
	GOOS=linux GOARCH=arm64 go build -ldflags="-s -w" -o bootstrap main.go
	chmod +x bootstrap  # Ensure executable permissions
	cp bootstrap $(ARTIFACTS_DIR)/  # SAM requires this copy
	@echo "✅ Built bootstrap binary"