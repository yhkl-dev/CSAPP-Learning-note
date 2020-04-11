(define (new-fib n)
	(cond ((= n 0) 0)
				((= n 1) 1)
				(else (+ (new-fib (- n 1))
								 (new-fib (- n 2))))))

(define (fib n)
	(fib-iter 1 0 n))

(define (fib-iter a b count)
	(if (= count 0)
			b
			(fib-iter (+ a b) a (- count 1))))

(define fi (/ (+ 1 (sqrt 5)) 2))

(define (good-enough? n)
	(< (abs (- (fib n) (/ (fin fi n) (sqrt 5)))) 0.0001))

(define (abs x)
	(if (< x 0) 
			(- x)
			x))

(define (fin fi n)
	(if (= n 0) 
			1
			(* fi (fin fi (- n 1)))))

(define (expt fi n)
	(expt-iter fi n 1)
	)

(define (expt-iter fi counter product)
	(if (= counter 0)
			product
			(expt-iter fi
								 (- counter 1)
								 (* fi product))))
						
