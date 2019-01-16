
#!/bin/bash

for file in *; do

	if [ -f "$file" ]; then
		echo "$file"
	else
		if [ $file = "outs" ]; then
			echo "outs"
		else
			echo "$file/out.jpg"
			cp "$file/out.jpg" "outs/$file.out.jpg"
		fi
	fi
done
