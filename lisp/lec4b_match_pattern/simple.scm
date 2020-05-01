(define (simplify-exp exp)
	(try-rules
		(if (command? exp)
				(map simplify-exp exp)
				exp)))
