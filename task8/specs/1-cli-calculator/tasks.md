---

description: "Task list for CLI Calculator feature implementation"
---

# Tasks: CLI Calculator

**Input**: Design documents from `/specs/1-cli-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, quickstart.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Paths shown below assume single project as per plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize project with `uv init` to create `pyproject.toml` and default structure.
- [x] T002 [P] Create `calculator/__init__.py`.
- [x] T003 [P] Create `calculator/main.py`.
- [x] T004 [P] Create `calculator/parser.py`.
- [x] T005 [P] Create `calculator/operations.py`.
- [x] T006 [P] Create `tests/test_operations.py`.
- [x] T007 [P] Create `tests/test_parser.py`.
- [x] T008 [P] Create `tests/test_cli.py`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T009 Set up `pytest` configuration in `pyproject.toml` or `pytest.ini`.
- [x] T010 Implement basic CLI loop (read input, process, print result) in `calculator/main.py`. This will be refined in later phases.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to perform basic arithmetic operations (addition, subtraction, multiplication, division) on integers and floating-point numbers through a command-line interface.

**Independent Test**: Can be fully tested by entering various valid expressions and verifying the output (e.g., "3 + 4" -> "7", "10.5 / 2" -> "5.25").

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T011 [P] [US1] Add unit tests for `add`, `subtract`, `multiply`, `divide` functions in `tests/test_operations.py`.
- [x] T012 [P] [US1] Add unit tests for valid basic arithmetic expressions parsing in `tests/test_parser.py`.
- [x] T013 [P] [US1] Add integration tests for basic arithmetic operations in `tests/test_cli.py`.

### Implementation for User Story 1

- [x] T014 [P] [US1] Implement `add`, `subtract`, `multiply`, `divide` functions in `calculator/operations.py`.
- [x] T015 [US1] Implement basic expression parsing for infix notation (operand operator operand) in `calculator/parser.py`.
- [x] T016 [US1] Integrate parser and operations in `calculator/main.py` to evaluate expressions.
- [x] T017 [US1] Implement display formatting for results: rounded to 6 decimal places, trim trailing zeros in `calculator/main.py` (or a display utility).

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Handle Invalid Inputs Gracefully (Priority: P1)

**Goal**: As a user, I want the calculator to provide clear error messages and not crash when I enter invalid expressions or commands.

**Independent Test**: Can be fully tested by entering various invalid inputs and observing error messages and program stability (e.g., "3 ++ 2" -> "Error: invalid expression.", "5 / 0" -> "Error: Division by zero.").

### Tests for User Story 2

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T018 [P] [US2] Add unit tests for division by zero error handling in `tests/test_operations.py`.
- [x] T019 [P] [US2] Add unit tests for invalid syntax, unsupported characters, and multiple operators parsing in `tests/test_parser.py`.
- [x] T020 [P] [US2] Add integration tests for various invalid inputs in `tests/test_cli.py`.

### Implementation for User Story 2

- [x] T021 [US2] Implement error handling for division by zero in `calculator/operations.py`.
- [x] T022 [US2] Implement input validation for invalid syntax, unsupported characters, and multiple operators without operands in `calculator/parser.py`.
- [x] T023 [US2] Integrate error messages from parser/operations into `calculator/main.py` for user display.
- [x] T024 [US2] Implement handling for empty input (re-prompt) in `calculator/main.py`.
- [x] T025 [US2] Implement handling for expressions with leading/trailing spaces in `calculator/parser.py` (e.g., stripping spaces).

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Access Help and Exit (Priority: P2)

**Goal**: As a user, I want to be able to view supported operations and gracefully exit the calculator.

**Independent Test**: Can be fully tested by entering "help", "exit", or "quit" and verifying the expected behavior (help message or program termination).

### Tests for User Story 3

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T026 [P] [US3] Add integration tests for `help` command in `tests/test_cli.py`.
- [x] T027 [P] [US3] Add integration tests for `exit` and `quit` commands in `tests/test_cli.py`.

### Implementation for User Story 3

- [x] T028 [US3] Implement `help` command logic to display supported operations and examples in `calculator/main.py`.
- [x] T029 [US3] Implement `exit` and `quit` command handling to terminate the program gracefully in `calculator/main.py`.

**Checkpoint**: All user stories should now be independently functional

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and overall code quality

- [x] T030 Implement warning for numbers approaching Python's `float` min/max limits in `calculator/operations.py` (or `main.py`).
- [x] T031 Ensure all code adheres to Python 3.12+ with comprehensive type hints.
- [x] T032 Verify no external libraries for evaluation (e.g., `eval()`) are used.
- [x] T033 Ensure errors are logged to console/stderr (FR-032).
- [x] T034 Achieve minimum 80% test coverage across the project.
- [x] T035 Code cleanup and refactoring for readability and maintainability.
- [ ] T036 Run quickstart.md validation (manually follow quickstart steps).

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories. Builds upon the parsing and evaluation framework.
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories.

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Core logic before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members (e.g., US1 and US2 can be developed concurrently after Foundational phase).

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Add unit tests for add, subtract, multiply, divide functions in tests/test_operations.py"
Task: "Add unit tests for valid basic arithmetic expressions parsing in tests/test_parser.py"
Task: "Add integration tests for basic arithmetic operations in tests/test_cli.py"
```

## Parallel Example: User Story 2

```bash
# Launch all tests for User Story 2 together:
Task: "Add unit tests for division by zero error handling in tests/test_operations.py"
Task: "Add unit tests for invalid syntax, unsupported characters, and multiple operators parsing in tests/test_parser.py"
Task: "Add integration tests for various invalid inputs in tests/test_cli.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
