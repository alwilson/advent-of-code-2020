module test;
	wire equal_2020;
	wire [25:0] product;

	// Simple clock
	reg clk = 0;
	always #5 clk = !clk;

	reg reset;

	reg [15:0] input_vals [0:255];
	reg [7:0] count = 0;

	reg [15:0] data;
	reg data_valid;

	initial begin
		// Dump waves
		// $dumpfile("part1.vcd");
		// $dumpvars(0, d1);
		
		// Initialize input memory
		$readmemh("input_hex.mem", input_vals);

		// Toggle reset
		# 0 reset = 1;
		# 210 reset = 0;
	end

	day1 d1 (clk, reset, equal_2020, product, data, data_valid);

	always @(posedge clk) begin
		// Stop sim once product is calculated
		if (equal_2020) begin
			#5 $display("product: %d", product);
			$finish;
		end

		if (reset) begin
			data <= 0;
			data_valid <= 0;
		end else begin
			if (count < 200) begin
				data <= input_vals[count];
				data_valid <= 1;
				count <= count + 1;
			end else begin
				data_valid <= 0;
			end
		end
	end
endmodule

// FIXME pass in input values from testbench!
module day1 (clk, reset, equal_2020, product, data, data_valid);
	input clk, reset;
	output equal_2020;
	output [25:0] product;
	input [15:0] data;
	input data_valid;

	wire clk, reset;
	reg [15:0] input_vals [0:255]; // FIXME treat this like actual memory...
	reg [15:0] input_val;
	reg [15:0] lookup_idx;

	reg lookup_table [0:2047]; // FIXME this one as well
	reg equal_2020;
	reg [25:0] product;

	integer i;
	initial begin
		// Clear lookup table entries
		for (i=0; i <= 2047; i=i+1)
			lookup_table[i] = 0;

		// Initialize input memory
		$readmemh("input_hex.mem", input_vals);
	end

	// Count to 200, assert bit, keep counting
	wire [9:0] value;
	wire table_updated;
	counter200 c1 (value, table_updated, clk, reset);

	reg [9:0] tb_rd_addr;
	wire      tb_rd_data;
	reg [9:0] tb_wr_addr;
	reg       tb_wr_data;
	reg       tb_wr_en;
	always @(posedge reset) begin
		if (reset) begin
			tb_rd_addr <= 0;
			tb_wr_addr <= 0;
			tb_wr_data <= 0;
			tb_wr_en   <= 0;
		end
	end
	ram #(10, 1) tb1 (clk, reset, tb_rd_addr, tb_rd_data, tb_wr_addr, tb_wr_data, tb_wr_en);
	
	reg  [7:0]  input_rd_addr;
	wire [15:0] input_rd_data;
	reg  [7:0]  input_wr_addr;
	reg  [15:0] input_wr_data;
	reg         input_wr_en;
	always @(posedge reset) begin
		if (reset) begin
			input_rd_addr <= 0;
			input_wr_addr <= 0;
			input_wr_data <= 0;
			input_wr_en   <= 0;
		end
	end
	ram #(8, 16) input1 (clk, reset, input_rd_addr, input_rd_data, input_wr_addr, input_wr_data, input_wr_en);

	always @(posedge clk or posedge reset) begin
		if (reset) begin
			equal_2020 <= 0;
			product <= 0;
			input_val <= 0;
			lookup_idx <= 0;
		end else begin
			if (table_updated) begin
				// Walk input memory and look for satisfying lookup table entries
				equal_2020 <= lookup_table[2020 - input_vals[value]];
				input_val <= input_vals[value];
				lookup_idx <= 2020 - input_vals[value];
				product <= input_val * lookup_idx;
			end else begin
				// Read input memory and fill in lookup table
				equal_2020 <= 0;
				lookup_table[input_vals[value]] <= 1;

				if (data_valid) begin
					tb_wr_addr <= data;
					tb_wr_data <= 1;
					tb_wr_en <= 1;
					input_wr_addr <= value;
					input_wr_data <= data;
					input_wr_en <= 1;
				end else begin
					tb_wr_en <= 0;
					input_wr_en <= 0;
				end
			end
		end
	end
endmodule

module ram (clk, reset, rd_addr, rd_data, wr_addr, wr_data, wr_en);
	parameter addr_size = 1;
	parameter word_size = 1;

	input clk, reset;
	input [addr_size-1:0] rd_addr;
	output [word_size-1:0] rd_data;
	input [addr_size-1:0] wr_addr;
	input [word_size-1:0] wr_data;
	input wr_en;

	wire [addr_size-1:0] rd_addr;
	reg [word_size-1:0] rd_data;
	wire [addr_size-1:0] wr_addr;
	wire [word_size-1:0] wr_data;
	wire wr_en;

	reg [word_size-1:0] mem [0:(1<<addr_size)-1];
	reg [addr_size-1:0] clr_addr;
	reg reset_triggered;

	always @(posedge clk or posedge reset) begin
		if (reset) begin
			clr_addr <= 0;
			rd_data <= 0;
			reset_triggered <= 1;
		end else if (reset_triggered) begin
			mem[clr_addr] <= 0;
			if (clr_addr == addr_size**2-1) begin
				clr_addr <= clr_addr + 1;
			end else begin
				clr_addr <= 0;
				reset_triggered <= 0;
			end
		end else begin
			if (wr_en) begin
				mem[wr_addr] <= wr_data;
				rd_data <= wr_data;
			end else begin
				rd_data <= mem[rd_addr];
			end
		end
	end
endmodule
