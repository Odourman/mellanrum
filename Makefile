.PHONY: all model check clean
all: build/mellanrum_ntsc.bin
build/mellanrum_ntsc.bin: rom/src/main.asm rom/src/data.inc
	mkdir -p build
	dasm rom/src/main.asm -f3 -obuild/mellanrum_ntsc.bin -lbuild/mellanrum_ntsc.lst -sbuild/mellanrum_ntsc.sym
	python3 scripts/check_rom.py build/mellanrum_ntsc.bin
model:
	(cd reference && python3 -m unittest -q test_engine.py)
	python3 scripts/generate_rom_data.py --original reference/rooms.json --graphics graphics --output rom/src/data.inc --check
check: all model
	python3 scripts/check_rom_vs_model.py
clean:
	rm -rf build
