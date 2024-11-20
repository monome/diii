print("METRO TEST ======")
grid_led_all(0)
grid_led(0,0,15)
grid_refresh()

ccval = {0, 0, 0, 0, 0, 0, 0, 0}
ccnum = {10, 11, 12, 13, 14, 15, 16, 17}

metro = function(index, count)
	--print(string.format("metro %d: %d", index, count))
	grid_led(count,index,3)
	grid_refresh()
	--midi_tx(0, 0xb0, ccnum[index], ccval[index])
	ccval[index] = (ccval[index] + 1) % 128
end

grid = function(x,y,z)
	--print(string.format("%d %d %d",x,y,z))
	note = x + (7-y)*5 + 50
	midi_tx(0, 0x91, note, z*127)
	grid_led(x,y,z*15)
	grid_refresh()
end

metro_set(1, 100, 5)
metro_set(2, 50, 10)
