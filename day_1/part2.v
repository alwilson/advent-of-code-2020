module day1;
	reg reset;
	reg [15:0] input_vals [0:255];
	reg [15:0] input_val;
	reg [15:0] lookup_idx;

	reg lookup_table [0:2047];
	reg equal_2020;
	reg [40:0] product;

	integer i;
	initial begin
		// Dump waves
		// $dumpfile("part1.vcd");
		// $dumpvars(0, day1);

		// Clear lookup table entries
		for (i=0; i <= 2047; i=i+1)
			lookup_table[i] = 0;

		// Initialize input memory
		$readmemh("input_hex.mem", input_vals);

		// Toggle reset
		# 0 reset = 1;
		# 0 reset = 0;
	end

	// Simple clock
	reg clk = 0;
	always #5 clk = !clk;

	// Count to 200, assert bit, keep counting
	wire [9:0] value;
	wire table_updated;
	counter200 c1 (value, table_updated, clk, reset);

	// Second input value to compare against
	reg [15:0] value2;
	reg [15:0] input_val2;
	always @(posedge clk or posedge reset) begin
		if (reset) begin
			equal_2020 <= 0;
			product <= 0;
			input_val <= 0;
			value2 <= 0;
			input_val2 <= 0;
			lookup_idx <= 0;
		end else begin
			if (table_updated) begin
				// Walk input memory and look for satisfying lookup table entries
				if ((value != value2) && (input_vals[value] + input_vals[value2] <= 2020)) begin
					equal_2020 <= lookup_table[2020 - input_vals[value] - input_vals[value2]];
					input_val <= input_vals[value];
					input_val2 <= input_vals[value2];
					lookup_idx <= 2020 - input_vals[value] - input_vals[value2];
				end
				product <= input_val * input_val2 * lookup_idx;

				// Advance second value by 1 every loop (hacky?)
				if (value >= 199) begin
					value2 <= value2 + 1;
				end
			end else begin
				// Read input memory and fill in lookup table
				equal_2020 <= 0;
				lookup_table[input_vals[value]] <= 1;
			end

			// Stop sim once product is calculated
			if (equal_2020) begin
				#5 $display("product: %d", product);
				$finish;
			end
		end
	end
endmodule
