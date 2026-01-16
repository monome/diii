print("step")

alt = 0

ch = 0
step = 1
last = 0
note = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
map = {66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96}

tick = function()
	if last > 0 then midi_note_off(map[last]) end
  if cut then
    step = cut
    cut = nil
  else
    step = (step % 16) + 1
  end
	last = note[step]
	if last > 0 then midi_note_on(map[last]) end
	redraw()
end

m = metro.init(tick, .1)

event_grid = function(x,y,z)
	if y==1 then
		if x==16 then
      alt = z
    end
  elseif y==2 and z==1 then
    cut = x
	elseif z == 1 then
		if note[x] == y then note[x] = 0
		else note[x] = y end
		redraw()
	end
end

redraw = function()
	grid_led_all(0)
	grid_led(step,2,5)
	for n=3,16 do
		if note[n] > 0 then
			grid_led(n,note[n],step==n and 15 or 5)
		end
	end
	grid_refresh()
end

ticks = 0

midi_rx = function(d1,d2,d3,d4)
	if d1==8 and d2==240 then
		ticks = ((ticks + 1) % 12)
		if ticks == 0 then tick() end
	else
		ps("midi_rx %d %d %d %d",d1,d2,d3,d4)
	end
	--print("midi",d1,d2,d3,d4)
end

redraw()

m:start()
