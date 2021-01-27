// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"strconv"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
	"github.com/go-openapi/validate"
)

// Port port
//
// swagger:model Port
type Port struct {

	// connected port
	ConnectedPort *Href `json:"connected_port,omitempty"`

	// data
	Data interface{} `json:"data,omitempty"`

	// hardware
	Hardware *Href `json:"hardware,omitempty"`

	// href
	Href string `json:"href,omitempty"`

	// id
	// Format: uuid
	ID strfmt.UUID `json:"id,omitempty"`

	// name
	Name string `json:"name,omitempty"`

	// type
	Type string `json:"type,omitempty"`

	// virtual networks
	VirtualNetworks []*Href `json:"virtual_networks"`
}

// Validate validates this port
func (m *Port) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateConnectedPort(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateHardware(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateID(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateVirtualNetworks(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *Port) validateConnectedPort(formats strfmt.Registry) error {

	if swag.IsZero(m.ConnectedPort) { // not required
		return nil
	}

	if m.ConnectedPort != nil {
		if err := m.ConnectedPort.Validate(formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("connected_port")
			}
			return err
		}
	}

	return nil
}

func (m *Port) validateHardware(formats strfmt.Registry) error {

	if swag.IsZero(m.Hardware) { // not required
		return nil
	}

	if m.Hardware != nil {
		if err := m.Hardware.Validate(formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("hardware")
			}
			return err
		}
	}

	return nil
}

func (m *Port) validateID(formats strfmt.Registry) error {

	if swag.IsZero(m.ID) { // not required
		return nil
	}

	if err := validate.FormatOf("id", "body", "uuid", m.ID.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *Port) validateVirtualNetworks(formats strfmt.Registry) error {

	if swag.IsZero(m.VirtualNetworks) { // not required
		return nil
	}

	for i := 0; i < len(m.VirtualNetworks); i++ {
		if swag.IsZero(m.VirtualNetworks[i]) { // not required
			continue
		}

		if m.VirtualNetworks[i] != nil {
			if err := m.VirtualNetworks[i].Validate(formats); err != nil {
				if ve, ok := err.(*errors.Validation); ok {
					return ve.ValidateName("virtual_networks" + "." + strconv.Itoa(i))
				}
				return err
			}
		}

	}

	return nil
}

// MarshalBinary interface implementation
func (m *Port) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *Port) UnmarshalBinary(b []byte) error {
	var res Port
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}