(define (timed-prime-test n)
	(newline)
	(display n)
	(start-prime-test n (runtime)))

(define (start-prime-test n start-time)
	(if (prime? n)
			(report-time (- (runtime) start-time))))

(define (report-time elapsed-time)
	(display " *** ")
	(display elapsed-time))
