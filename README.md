# Rektify AI
Dynamic code analysis tool powered by machine learning to enable optimal security smart contracts. As the blockchain space grows, so does the amount of rich data-points generated from technical attacks. 

The more data that is collected on isolated attack instances on protocols, the more likely we can train models to defend against attacks similar to the adversarial attack framework used against ML models.

<b> Languages: </b>
- Solidity (EVM-bytecode)
- Rust
- Vyper

<b> Auditing Framework </b>
- New Audit
  - New project that has not received an audit before
- Repeat Audit
  - A project that has had a previous audit from your firm comes back again. New features.
- Fix Audit
  - Review fix of bug(s) from prior audit(s)
- Retainer Audit
  - Constantly reviewing project updates
- Incident Audit
  - Comprehensive exploit review

<b> Code Analyses Techniques </b>
- Specification Analysis
  - Auditor analyzes it manually.
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

