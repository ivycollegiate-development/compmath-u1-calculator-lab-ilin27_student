# journal-0921-$(whoami).md
# Replace the bracketed lines below with your own answers.
# Keep the two questions as headings.

## Which Python tool is most important for security?

Input validation is the most important tool for security because it acts as the proactive first line of defense before untrusted data can reach the system. While try/except catches runtime crashes and type conversion only formats data types, input validation actively enforces boundaries and business rules to prevent dangerous or quietly wrong values. Without rigorous validation, a program may not crash, but it can still execute harmful or logically invalid operations.

## Is a completely crash-proof program possible?
A completely crash-proof program is theoretically impossible because developers cannot foresee every conceivable edge case, malicious input, or unexpected hardware and environment failure. The class discussion shifted my perspective from aiming for complete perfection to practicing defensive programming, which aims to make a program "less unsafe." Instead of silently failing or hiding problems, a good program must fail gracefully and communicate honestly with the user.

