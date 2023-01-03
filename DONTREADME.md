# Rektify AI
Dynamic code analysis tool powered by machine learning to enable optimal security smart contracts. As the blockchcain space grows, so does the amount of rich data-points generated from technical attacks. The more data that is collected on isolated attack instances on protocols, the more likely we can train models to defend against attacks in an adversarial attack frameowork.

Languages: 
- Solidity (EVM-bytecode)
- Go
- Rust
- Clarity (smart contracts on Bitcoin)
- sCrypto (smart contracts on Bitcoin SV)

Auditing Framework
- New Audit
  - New project that has not recieved an audit before
- Repeat Audit
  - A project that has had a previous audit from your firm comes back again. New features.
- Fix Audit
  - Review fix of bug(s) from prior audit(s)
- Retainer Audit
  - Constantly reviewing project updates
- Incident Audit
  - Exploit review

Code Analyses Techniques
- Specification Analysis
  - Auditor analizes it manually.
  - Specification that this code does exactly what it is supposed to do.
- Doc Analysis
  - Smart contracts should use NatSpec
- Static Analysis
  - Technique of anlyzing program properties withous actually executing the program
- Property-based testing
  - Known as fuzzing
  - Provides huge amount of random and unexpected input values to smart contract functions in order to break them (crashes, uncaught exceptions, memory leaks, etc.)
  - Tools: Echidna, Foundry built-in fuzzer, Harvey
- Symbolic Analysis
  - Technique of checking for program correctness, by using symbolic inputs to represent set 
