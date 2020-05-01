(define (smallest-divisor n)
	(find-divisor n 2))

(define (find-divisor n test-divisor)
	(cond ((> (square test-divisor) n) n)
				((divedes? test-divisor n) test-divisor)
				(else (find-divisor n (+ test-divisor)))))

(define (prime? n)
	(= n (smallest-divisor n)))

(define (timed-prime-test n)
	(newline)
	(display n)
	(start-prime-test n (runtime)))

(define (start-prime-test n start-time)
	(if (prime? n)
			(report-prime (- (runtime) start-time))))

(define (report-prime elapsed-time)
	(display " ***")
	(display elapsed-time))
