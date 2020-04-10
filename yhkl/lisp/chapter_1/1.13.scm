(define (fib n)
	(fib-iter 1 0 n))

(define (fib-iter a b count)
	(if (= count 0)
			b
			(fib-iter (+ a b) a (- count 1))))

(define fi (/ (+ 1 (sqrt 5)) 2))

(define (goog-enough? fib fi)
	(< (abs (- fib fi)) 0))

(define (abs x)
	(if (< x 0) 
			(- x)
			x))


