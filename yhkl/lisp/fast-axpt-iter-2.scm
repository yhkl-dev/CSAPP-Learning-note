(define (fast-expt b n)
  (iter 1 b n))

(define (iter a b n) 
  (cond ((= n 0) a)
	((even? n) (iter a (* b b) (/ n 2)))
	(else (iter (* a b) b (- n 1)))))



