# Nymix: Decentralized Network Telemetry Protocol (MVP)

Nymix is a decentralized physical infrastructure network (DePIN) designed for crowdsourced residential internet quality and network performance monitoring. By running lightweight local telemetry nodes, independent operators contribute real-time connectivity data—such as latency, availability, and bandwidth—directly from their residential connections. 

This protocol acts as an open, tamper-proof network health ledger that decentralized applications (dApps), Oracle networks, and RPC providers can leverage to maintain high availability and evaluate node routing performance globally.

---

## Current MVP Architecture

This repository contains the functional pre-seed MVP architecture running a localized simulation environment:

*   **Backend (`server.py`):** Built with Flask (Python 3). It handles incoming node telemetry submissions, calculates reward point allocations, and hosts localized database sessions in memory.
*   **Anti-Farming Heuristics:** Implements a native IP-based rate limiting restriction (30-minute cooling down period per unique address) to mitigate sybil attacks, request spamming, and malicious reward extraction.
*   **Unified Frontend (`index.html`):** A dark-themed responsive user interface managing cryptographic wallet anchor simulations, automated network diagnostic triggers, and localized telemetry state visualizations.

---

## Local Development Setup

### Prerequisites
Ensure you have a localized Python 3 environment active along with the required web microframework dependency:

```bash
pip install flask
