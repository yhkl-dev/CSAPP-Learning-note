; http://www.yangkai.org.cn/2020/04/11/%E8%AF%81%E6%98%8EFib-n-%E6%98%AF%E6%9C%80%E6%8E%A5%E8%BF%91%CE%A6-n-%E2%88%9A5-%E5%85%B6%E4%B8%AD%CE%A6-%EF%BC%881-%E2%88%9A5-2/
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
						
