module counter200(out, rollover, clk, reset);
	output [9:0] out;
	output rollover;
	input clk, reset;

	reg [9:0] out;
	reg rollover;
	wire clk, reset;

	always @(posedge clk or posedge reset) begin
		if (reset) begin
			out <= 0;
			rollover <= 0;
		end else if (out >= 199) begin
			out <= 0;
			rollover <= 1;
		end else begin
			out <= out + 1;
		end
	end

endmodule
