awk -F"\t" 'BEGIN{last_str="a";last_sum=0;}
	{if($1!=last_str)
		{print last_str"\t"last_sum; 
			last_str=$1;last_sum=$2;}
	else {last_sum+=$2;} 
	}
	END{print last_str"\t"last_sum;}'
