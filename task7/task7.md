# Spec-Kit Plus:

Spec-kit plus is an SDD-RI (specification-Driven Development with Reusable Intelligence) framework build around one core idea.
     "capture intelligence, not just deliver code."
The philosophy behind the spec-kit plus states that Every feature we build produce 2 distinct output.
1. Working code(Temporary): The feature that works today, its tied to the current tech stack, can be rewritten anytime, and does not retain long term value.
2. Reusable Intelligence(Permanent): The reasoning, decision framework and prompt patterns behind the code. It applies across project and evolves over time, stored in history/ as a lasting personal knowledge base.
Spec-kit plus is a methodology framework that work with your AI tool (Claude code, Gemini CLI etc). It activates AI tools reasoning capabilities through structured workflows.

# 5 Core Concepts Of Spec-Kit Plus:
five slash commands represent the core concepts of SDD-RI workflow, implemented by spec-kit plus.

# 1. /Constitution:

The constitution is Rulebook and project-wide quality standards that lists the most important rules that both you and AI must follow, no matter what.
/sp.constitution command create the constitution.md file. The constitution act as the foundation  that shapes specification, planning and execution.

# 2. /Specify:

Writing complete specification, A good spec clearly states the intent of the project, set explicit and testable constraints and defines measurable success criteria that the AI can use to build acceptance tests. 
It also aligns fully with the constitution, ensuring all work follows your established standards.In AI-native development ability to write a clear specification is more valuable than your ability to write code.

# 3. /Plan:

Once the specification is ready the plan phase figures out how to actualy build it. /sp.plan commands analyzes the specification and generate a detailed implementation plan by breaking spec into components, ordering dependencies,
identifiying design decisions and proposing architecture.

# 4. /Tasks:

Tasks phase has Atomic work units and checkpoints pattern. The /sp.tasks command analyzes the specification and plan, then generates a complete task breakdown that includes, Each task is 15-30 minutes unit with single and clear
acceptance criterion and produces a verifiable output. Check point pattern allow human to control the workflow.We not write tasks from scratch. /sp.tasks command writes them for us based on our specification and plan.
our jobs is to understand the task struture, validate its atomic unit, and execute it with checkpoints.

# 5. /Implement:

Implementation isn’t Autonomous execution.It is a collaborative process where you decide direction, the AI executes the steps, and both of you verify progress against the specification. When /sp.implement runs, it reads your tasks.md file,
executes tasks in dependency order, and presents outputs and intermediate results at defined checkpoints. At each checkpoint, the agent pauses for your review and approval, ensuring you stay in control while the AI handles the execution.









