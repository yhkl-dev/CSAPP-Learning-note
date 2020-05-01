
(define (calculate a b)
	(calculate-iter a b 0)	
  )

(define (even? n)
	(= (remainder n 2) 0)
	)

(define (double a)
	(+ a a)
	)

(define (havle b)
	(/ b 2)
	)

(define (calculate-iter a b res)
	(cond ((= b 0) res)
				((even? b) (calculate-iter (double a) (havle b) res))
				(else (calculate-iter a (- b 1) (+ res a)))
	))
