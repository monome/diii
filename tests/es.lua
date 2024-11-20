print("earthsea?")
grid_led_all(0)
grid_led(0,0,15)
grid_refresh()

ch = 0

metro = function(index, count)
	--print(string.format("metro %d: %d", index, count))
	--grid_led(count,index,3)
	--grid_refresh()
end

grid = function(x,y,z)
	--print(string.format("%d %d %d",x,y,z))
	if x==0 then
		if z then
			grid_led(0,ch,0)
			ch=y
			grid_led(0,ch,3)
			grid_refresh()	
		end
	else

	note = x + (7-y)*5 + 50
	midi_tx(0, 0x90+ch, note, z*127)
	grid_led(x,y,z*15)
	grid_refresh()
end
end

--metro_set(1, 100, 5)
--metro_set(2, 50, 10)
