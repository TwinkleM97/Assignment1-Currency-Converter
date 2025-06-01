# Use Python 3.9 slim as the base image
FROM python:3.9-slim

# Set metadata
LABEL maintainer="Twinkle Mishra"
LABEL description="Currency Converter Application for PROG8860 Assignment"
LABEL version="1.0"

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV APP_ENV=production
ENV API_ENDPOINT=localhost:8080

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy files
COPY currency_converter.py .
COPY test_currency_converter.py .

# Set permissions
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port 
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "from currency_converter import CurrencyConverter; c = CurrencyConverter(); print('Health check OK')" || exit 1

# Default command
CMD ["python3", "currency_converter.py"]
