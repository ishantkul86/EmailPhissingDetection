# Phishing RAG

A research prototype for phishing email detection using
LLMs, personalized RAG, and local inference.

## Research Question

Can a small locally deployed LLM enhanced with personalized
RAG provide effective phishing email detection while
preserving privacy and reducing inference cost?

## Current Stage

Day 1: LLM-only baseline.

## Current Architecture

```text
Email
  |
  v
PhishingDetector
  |
  v
LLMProvider
  |
  v
OllamaProvider
  |
  v
Ollama
  |
  v
Local LLM
  |
  v
Structured JSON