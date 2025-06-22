print("earthsea?")

fs_run_file('mu.lua')

grid_led_all(0)
grid_led(1,1,3)
grid_refresh()

ch = 1
sc= 1
scale = mu.generate_scale(50,sc,2)

event_grid = function(x,y,z)
	--print(string.format("%d %d %d",x,y,z))
	if x==1 then
		if z then
			grid_led(1,ch,0)
			ch=y
			grid_led(1,ch,3)
			grid_refresh()	
		end
	elseif x==2 then
		if z then
			grid_led(2,sc,0)
			sc=y
			scale = mu.generate_scale(50,sc,2)
			grid_led(2,sc,3)
			grid_refresh()	
		end
	else
		--note = x + (7-y)*5 + 50
		note = scale[x-2]
		print(note,z)
		if z>0 then midi_note_on(note) else midi_note_off(note) end
		--midi_tx(0, 0x90+ch-1, note, z*127)
		grid_led(x,y,z*15)
		grid_refresh()
	end
end
